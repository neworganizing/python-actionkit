from datetime import datetime
import re
import psycopg2
import settings
import unittest
import utils

class PaymentUrlGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.token_id = '3nmqoul2'
        self.user_id = '.' + '18715613'
        self.datetime_format = '%Y%m%d%H%M'
        self.hash_separator = '.'
        self.braintree_secret = settings.BRAINTREE_ONECLICK_SECRET
        self.ak_secret = settings.AK_SECRET
        self.db_connection = db_connection=psycopg2.connect(
            dbname=settings.REDSHIFT_DATABASE,
            host=settings.REDSHIFT_HOST,
            port= settings.REDSHIFT_PORT,
            user= settings.REDSHIFT_USER,
            password= settings.REDSHIFT_PASSWORD
        )
        self.ak_secret = settings.AK_SECRET
        self.braintree_secret = settings.BRAINTREE_ONECLICK_SECRET
        self.base_url = 'https://act.moveon.org/donate/civ-donation-quickpay?payment_hash='
    def test_quickpay_url(self): #all of these values depend on that user being the specific one it is.
        url = utils.quickpay_url(self.datetime_format, self.user_id, self.hash_separator, self.db_connection, self.ak_secret, self.braintree_secret, self.base_url)
        self.assertIn("act.moveon.org/donate/civ-donation-quickpay?", url)
        self.assertIn("payment_hash=3nmqoul2", url)
        self.assertIn("&akid=.18715613", url)
        self.assertEqual(len(url), 128)

    def test_payment_hash(self):
        payment_hash = utils.payment_hash(self.token_id, self.datetime_format, self.braintree_secret, self.hash_separator)
        self.assertIn("3nmqoul2", payment_hash)
        self.assertRegexpMatches(payment_hash, ".{8}\.\d{12}\..{8}\..{10}")

    def test_append_hash(self):
        parts = [ self.token_id, '201901011111', '12345678']
        append_hash = utils._append_hash(self.hash_separator, self.braintree_secret, *parts)

    def test_oneclick_hash(self):
        contents = self.hash_separator.join([self.token_id, datetime.now().strftime(self.datetime_format), '01234567'])
        oneclick_hash = utils.oneclick_hash(self.braintree_secret, contents)

if __name__ == '__main__':
    unittest.main()
