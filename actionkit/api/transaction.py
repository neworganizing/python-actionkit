from actionkit.api.base import ActionKitAPI

class AKTransactionAPI(ActionKitAPI):

    def get_transaction_detail(self, transaction_id):
        """
            Get recurring donation info and billing info
        """
        if getattr(self.settings, 'AK_TEST', False):
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
