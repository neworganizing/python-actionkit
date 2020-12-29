import requests
from actionkit.api.base import ActionKitAPI
from actionkit.api.test_data import TEST_DATA

class AKOrderAPI(ActionKitAPI):

    def get_order_detail(self, order_id):
        """
            Get order and billing info
        """
        if getattr(self.settings, 'AK_TEST', True):
            if order_id and str(order_id) in TEST_DATA['orders']:
                order = TEST_DATA['orders'][str(order_id)]
                user_id = order['user']
                user_id = user_id.replace('/rest/v1/user/', '')
                user_id = user_id.replace('/','')
                user = TEST_DATA['users'][user_id]
                products = []
                if len(order['orderdetails']) > 0:
                    for details in order['orderdetails']:
                        orderdetail = TEST_DATA['orderdetails'][details]
                        product_id = orderdetail['product']
                        product_id = product_id.replace('/rest/v1/product/', '')
                        product_id = product_id.replace('/','')
                        products.append(TEST_DATA['products'][product_id])
                res = self.test_service_get_order(order, user, products)
            else:
                res = self.test_service_get_order(None, None, None)
            return res.data
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
            order_details = json.get('orderdetails')
            products = []
            for item in order_details:
                order_detail_res = self.client.get('%s%s' % (self.base_url, item))
                if order_detail_res.status_code == 200:
                    order_detail_json = order_detail_res.json()
                    if 'product' in order_detail_json:
                        product_detail = order_detail_json['product']
                        product_detail_res = self.client.get('%s%s' % (self.base_url, product_detail))
                        products.append(product_detail_res.json())
            rv['products'] = products
        return rv

    def list_orders(self, user_id=False, query_params={}):
        if getattr(self.settings, 'AK_TEST', True):
            if user_id and str(user_id) in TEST_DATA['users']:
                res = self.test_service_get_orders(TEST_DATA['users'][str(user_id)])
            else:
                res = self.test_service_get_orders(None)
            return {'res': res, 'objects': res.objects}
        if user_id:
            query_params['user'] = user_id
        result = self.client.get(
            '%s/rest/v1/order/' % (self.base_url),
            params = query_params
        )
        rv = {'res': result, 'objects': []}
        while result.status_code == 200:
            json = result.json()
            rv['objects'].extend(json.get('objects', []))
            next_page = json.get('meta', None).get('next', None)
            if next_page:
                result = self.client.get('%s%s' % (self.base_url, next_page))
            else:
                break
        return rv


    def reverse_order(self, order_id, agent_id=False):
        action_dictionary = []
        if agent_id:
            action_dictionary['action_agent_id'] = agent_id
        result = self.client.post(
            '%s/rest/v1/order/%s/reverse/' % (self.base_url, order_id),
            params = action_dictionary
        )
        return {'res': result}

    def test_service_get_orders(self, data):
        r = requests.Response()
        if data == None:
            r.objects = []
            r.status_code = 404
        else:
            r.status_code = 200
            r.objects = data['user']['orders']
        return r

    def test_service_get_order(self, order, user, products):
        r = requests.Response()
        if order == None:
            r.object = {}
            r.status_code = 404
        else:
            r.status_code = 200
            order['products'] = products
            order['user_detail'] = user
            r.data = order
        return r
