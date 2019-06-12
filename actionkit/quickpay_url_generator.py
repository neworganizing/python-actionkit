import settings
import utils

token_id = '3nmqoul2'
akid = '.18715613.pOX3Jq'
datetime_format = '%Y%m%d%H%M'
hash_separator = '.'
braintree_secret = settings.BRAINTREE_ONECLICK_SECRET
print utils.quickpay_url(token_id, datetime_format, akid, braintree_secret, hash_separator)

# investigate: is it possible to do keyword params in python?
# make sure tests work
# integrate akid generator
# write a thing to get a token_id from the redshift db
