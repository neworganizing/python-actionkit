import base64
import datetime
import hashlib
import random


def generate_payment_hash(token_id,
                          site='roboticdogs',
                          braintree_oneclick_secret='test123',
                          DATETIME_FORMAT='%Y%m%d%H%M',
                          HASH_SEP='.'):
    parts = [
        token_id,
        datetime.datetime.now().strftime(DATETIME_FORMAT),
        randstr32()[:8],
    ]
    parts_str = HASH_SEP.join(parts)
    return HASH_SEP.join([
        parts_str,
        oneclick_hash(parts_str, site, braintree_oneclick_secret).decode()[:10]
    ])

def randstr32():
    """returns base-32 encoded random garbage"""
    return ''.join([
        random.choice('abcdeghijklmnopqrstuvwxyz234567')
        for x in range(8)])

def oneclick_hash(contents, site, BRAINTREE_ONECLICK_SECRET):
    "Return a long base64 hash of contents, with secret and site"
    parts = [BRAINTREE_ONECLICK_SECRET, site, contents]
    sha = hashlib.sha256('-'.join(parts).encode())
    raw_hash = sha.digest()
    return base64.urlsafe_b64encode(raw_hash)
