import psycopg2
import settings
import utils

# aili's info: user_id is 18715613, token_id is 3nmqoul2
# adam's info: user_id is 8934025, token_id is khjnslz3

user_id = '.' + '7666955'


def get_array_of_payment_urls(user_ids): #user_ids must be array of user ids, eg: ['10388201', '10293901', '1023948']
    datetime_format = '%Y%m%d%H%M'
    hash_separator = '.'
    db_connection=psycopg2.connect(
        dbname=settings.REDSHIFT_DATABASE,
        host=settings.REDSHIFT_HOST,
        port= settings.REDSHIFT_PORT,
        user= settings.REDSHIFT_USER,
        password= settings.REDSHIFT_PASSWORD
    )
    ak_secret = settings.AK_SECRET
    braintree_secret = settings.BRAINTREE_ONECLICK_SECRET
    base_url = 'https://act.moveon.org/donate/civ-donation-quickpay?payment_hash='
    quickpay_urls = []
    for user_id in user_ids:
        user_id = '.' + user_id
        url = utils.quickpay_url(datetime_format, user_id, hash_separator, db_connection, ak_secret, braintree_secret, base_url)
        print(url)
        quickpay_urls.append(url)
    return quickpay_urls

print(get_array_of_payment_urls(['18715613', '8934025', '7666955']))
