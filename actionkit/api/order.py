from actionkit.api.base import ActionKitAPI

try:
    import urllib.parse
    encode_url = urllib.parse.urlencode
except ImportError:
    # python2
    import urllib
    encode_url = urllib.urlencode

class AKOrderAPI(ActionKitAPI):

    def get_order_detail(self, order_id):
        """
            Get order and billing info
        """
        result = self.client.get(
            '%s/rest/v1/order/%s' % (
                self.base_url, order_id))
        rv = {'res': result}

        if result.status_code == 200:
            json = result.json()
            rv.update(json)
            user_detail = json.get('user_detail')
            user_detail_res = self.client.get('%s%s' % (self.base_url, user_detail))
            if user_detail_res.status_code == 200:
                rv['user_detail'] = user_detail_res.json()
        return rv


    def list_orders(self, user_id=False, query_params={}):
        if user_id:
            result = self.client.get(
                '%s/rest/v1/order/?user=%s&%s' % (
                    self.base_url, user_id, encode_url(query_params)))
        else:
            result = self.client.get(
                '%s/rest/v1/order/?%s' % (
                    self.base_url, encode_url(query_params)))
        rv = {'res': result, 'objects': []}
        paginate = True
        while paginate:
            if result.status_code == 200:
                json = result.json()
                objects = json.get('objects', None)
                if objects:
                    rv['objects'].extend(objects)
                next_page = json.get('meta', None).get('next', None)
                if next_page:
                    result = self.client.get('%s%s' % (self.base_url, next_page))
                else:
                    paginate = False
            else:
                return rv
        return rv


    def reverse_order(self, order_id):
        result = self.client.post(
            '%s/rest/v1/order/%s/reverse/' % (self.base_url, order_id)
        )
        return {'res': result}
