import hashlib
import base64

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
    sha = hashlib.sha256('{}.{}'.format(ak_secret, cleartext).encode('ascii'))
    raw_hash = sha.digest()
    urlsafe_hash = base64.urlsafe_b64encode(raw_hash).decode('ascii')
    short_hash = urlsafe_hash[:6]

    return '.'.join([cleartext, short_hash])
