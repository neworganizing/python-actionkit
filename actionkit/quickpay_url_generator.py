import settings
import utils

# aili's info: user_id is 18715613, token_id is 3nmqoul2
# adam's info: user_id is 8934025, token_id is khjnslz3
token_id = 'khjnslz3'
user_id = '.' + '8934025'
datetime_format = '%Y%m%d%H%M'
hash_separator = '.'
braintree_secret = settings.BRAINTREE_ONECLICK_SECRET
ak_secret = settings.AK_SECRET
print utils.quickpay_url(token_id, datetime_format, user_id, braintree_secret, hash_separator, ak_secret)

# investigate: is it possible to do keyword params in python?
# make sure tests work
# integrate akid generator
# write a thing to get a token_id from the redshift db
