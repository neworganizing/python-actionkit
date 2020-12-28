import requests
from actionkit.api.test_data import TEST_DATA
from actionkit.api.base import ActionKitAPI

class AKTransactionAPI(ActionKitAPI):

    def get_transaction_detail(self, transaction_id):
        """
            Get recurring donation info and billing info
        """
        if getattr(self.settings, 'AK_TEST', False):
            transaction = TEST_DATA['transactions'][str(transaction_id)]
            res = self.test_service_get_transaction(transaction)
            return res.data
            return TEST_DATA.get('get_orderrecurring_detail')
        result = self.client.get(
            '%s/rest/v1/transaction/%s' % (
                self.base_url, transaction_id))
        rv = {'res': result}

        if result.status_code == 200:
            json = result.json()
            rv.update(json)
        return rv

    def reverse_transaction(self, transaction_id):
        result = self.client.post(
            '%s/rest/v1/transaction/%s/reverse/' % (self.base_url, transaction_id)
        )
        return {'res': result}
    def test_service_get_transaction(self, transaction):
        r = requests.Response()
        if transaction == None:
            r.transaction = {}
            r.status_code = 404
        else:
            r.status_code = 200
            r.data = transaction
        return r
