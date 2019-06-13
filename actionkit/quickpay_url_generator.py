# import numpy as np
import psycopg2
import settings
import utils

# aili's info: user_id is 18715613, token_id is 3nmqoul2
# adam's info: user_id is 8934025, token_id is khjnslz3

user_id = '.' + '7666955'


def get_array_of_payment_urls(user_ids): #user_ids must be array of user ids, eg: ['10388201', '10293901', '1023948']
    datetime_format = '%Y%m%d%H%M'
    hash_separator = '.'
    quickpay_urls = []
    for user_id in user_ids:
        user_id = '.' + user_id
        url = utils.quickpay_url(datetime_format, user_id, hash_separator)
        print(url)
        quickpay_urls.append(url)
    return quickpay_urls

print(get_array_of_payment_urls(['18715613', '8934025', '7666955']))
