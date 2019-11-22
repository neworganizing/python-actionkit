from actionkit.api.base import ActionKitAPI


class AKOrderAPI(ActionKitAPI):

    def reverse_order(self, order_id):
        result = self.client.post(
            '%s/rest/v1/order/%s/reverse/' % (self.base_url, order_id)
        )
        return {'res': result}
