import base64
import Crypto.Random
from datetime import datetime
import hashlib
import psycopg2
import re
import settings


def validate_akid(ak_secret, akid):
    # https://roboticdogs.actionkit.com/docs/manual/developer/hashing.html#how-to-verify-an-akid
    # pop off the input hash
    chunks = akid.split('.')
    input_hash = chunks.pop()
    cleartext = '.'.join(chunks)

    # run the hashing algorithm
    sha = hashlib.sha256('{}.{}'.format(ak_secret, cleartext).encode('ascii'))
    raw_hash = sha.digest()
    urlsafe_hash = base64.urlsafe_b64encode(raw_hash).decode('ascii')
    short_hash = urlsafe_hash[:6]

    # compare the results
    return input_hash == short_hash


def generate_akid(ak_secret, cleartext):
    sha = hashlib.sha256('{}.{}'.format(ak_secret, str(cleartext)).encode('ascii'))
    raw_hash = sha.digest()
    urlsafe_hash = base64.urlsafe_b64encode(raw_hash).decode('ascii')
    short_hash = urlsafe_hash[:6]

    return '.'.join([str(cleartext), short_hash])


def parse_akid(akid):
    # akids can be <user_id>.<hash> or <mailing_id>.<user_id>.<hash>
    akid_parsed = re.match(r'(\d+)?\.((\d+)\.)?', akid)
    if akid_parsed:
        first_id, middle, middle_id = akid_parsed.groups()
        return {'user_id': int(middle_id),
                'front': first_id if first_id else None}
    return {'user_id': None, 'front': None}


def generate_datemarked_akid(ak_secret, user_id, prefix='d'):
    """
    Generate a valid akid but instead of the prefix with a mailing ID, it will be date-based.
    ActionKit doesn't use these, but usefully, it can generate these with the following template code:
    {% right_now %}
    {% with logged_in_user.id|default:'' as user_id %}
    {% with now|date:'\P\R\E\F\I\Xymd.'|concatenate:user_id|custom_hash as special_datemarked_akid %}
      ... SOME LINK: example.com?usertoken={{ special_datemarked_akid }}
    {% endwith %}
    {% endwith %}
    assuming your prefix="PREFIX" (the \P\R\E\F\I\X part)
    Then, you can provide a link to pass a login/akid'd context to another application from ActionKit.
    """
    return generate_akid(ak_secret,
                         '{}.{}'.format('%s%s' % (prefix, datetime.datetime.utcnow().strftime('%y%m%d')),
                                        user_id))


def validate_datemarked_akid(ak_secret, akid, prefix='d', days_expire=8):
    """
    Validates tokens generated with generate_datemarked_akid() with standard validation and also fails after a certain date
    """
    # https://roboticdogs.actionkit.com/docs/manual/developer/hashing.html#how-to-verify-an-akid
    def date_in_range(akiddatestr):
        current = datetime.datetime.utcnow().date()
        akiddate = datetime.datetime.strptime(akiddatestr, '%y%m%d').date()
        return (abs((current-akiddate).days) < days_expire)
    return (
        #stop people from re-using akids from other purposes/emails
        akid.startswith(prefix)
        #token expires after a day (should we make it 3?)
        and date_in_range(akid[len(prefix):len(prefix) + 6])
        and validate_akid(ak_secret, akid))

# Aili's experiment below this line

def randstr32():
    """returns base-32 encoded random garbage"""
    return base64.b32encode(Crypto.Random.new().read(24)).lower()

def oneclick_hash(braintree_secret, contents):
    "Return a long base64 hash of contents, with secret and site"
    parts = [braintree_secret, 'moveon', contents]
    sha = hashlib.sha256('-'.join(parts))
    raw_hash = sha.digest()
    return base64.urlsafe_b64encode(raw_hash)

def _append_hash(hash_separator, braintree_secret, *parts):
    parts_str = hash_separator.join(parts)
    return hash_separator.join([parts_str, oneclick_hash(braintree_secret, parts_str)[:10]])

def payment_hash(token_id, datetime_format, braintree_secret, hash_separator):
    parts = [
        token_id,
        datetime.now().strftime(datetime_format),
        randstr32()[:8],
    ]
    return _append_hash(hash_separator, braintree_secret, *parts)

def generate_token_id(user_id):
    con=psycopg2.connect(
        dbname=settings.REDSHIFT_DATABASE,
        host=settings.REDSHIFT_HOST,
        port= settings.REDSHIFT_PORT,
        user= settings.REDSHIFT_USER,
        password= settings.REDSHIFT_PASSWORD
    )
    cur = con.cursor()
    cur.execute("SELECT token_id FROM ak_moveon.bto_paymenttoken WHERE user_id = '18715613' AND status ='active';")
    data = cur.fetchone()
    cur.close()
    con.close()
    return data[0]

def quickpay_url(datetime_format, user_id, hash_separator):
    ak_secret = settings.AK_SECRET
    braintree_secret = settings.BRAINTREE_ONECLICK_SECRET
    akid = generate_akid(ak_secret, user_id)
    token_id = generate_token_id(user_id)

    return 'https://act.moveon.org/donate/civ-donation-quickpay?payment_hash=' + payment_hash(token_id, datetime_format, braintree_secret, hash_separator) + '&akid=' + akid
