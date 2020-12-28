import requests
from actionkit.api.base import ActionKitAPI
from actionkit.api.test_data import TEST_DATA

class AKOrderRecurringAPI(ActionKitAPI):

    def get_orderrecurring_detail(self, orderrecurring_id):
        """
            Get recurring donation info and billing info
        """
        if getattr(self.settings, 'AK_TEST', False):
            if orderrecurring_id and str(orderrecurring_id) in TEST_DATA['orders_recurring']:
                order_recurring = TEST_DATA['orders_recurring'][str(orderrecurring_id)]
                user_id = order_recurring['user']
                user_id = user_id.replace('/rest/v1/user/', '')
                user_id = user_id.replace('/','')
                order_id = order_recurring['order']
                order_id = order_id.replace('/rest/v1/order/', '')
                order_id = order_id.replace('/','')
                order = TEST_DATA['orders'][order_id]
                # user = TEST_DATA['users'][user_id]['user']
                res = self.test_service_get_order_recurring(order_recurring, order)
                return res.data
        result = self.client.get(
            '%s/rest/v1/orderrecurring/%s' % (
                self.base_url, orderrecurring_id))
        rv = {'res': result}

        if result.status_code == 200:
            json = result.json()
            rv.update(json)
            order = json.get('order')
            order_res = self.client.get('%s%s' % (self.base_url, order))
            if order_res.status_code == 200:
                order_json = order_res.json()
                rv['order'] = order_json
                user_detail = order_json.get('user_detail')
                user_detail_res = self.client.get('%s%s' % (self.base_url, user_detail))
                if user_detail_res.status_code == 200:
                    rv['user_detail'] = user_detail_res.json()
        return rv


    def list_orderrecurring(self, user_id=False, query_params={}):
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA['orders_recurring'].get(str(user_id))
        if user_id:
            query_params['user'] = user_id
        result = self.client.get(
            '%s/rest/v1/orderrecurring/' % (self.base_url),
            params=query_params
        )
        rv = {'res': result, 'orders_recurring': []}
        while result.status_code == 200:
            json = result.json()
            rv['orders_recurring'].extend(json.get('objects', []))
            next_page = json.get('meta', None).get('next', None)
            if next_page:
                result = self.client.get('%s%s' % (self.base_url, next_page))
            else:
                break
        return rv


    def cancel_orderrecurring(self, orderrecurring_id):
        result = self.client.post(
            '%s/rest/v1/orderrecurring/%s/cancel/' % (self.base_url, orderrecurring_id)
        )
        return {'res': result}

    def update_orderrecurring_status(self, orderrecurring_id, status):
        """
            Use ONLY to patch the status field.
            DO NOT use this to cancel a recurring donation; use the
            cancel_orderrecurring method instead, and then optionally
            use this method to patch the status.
            To change a recurring donation amount, cancel the existing
            recurring donation and create a new one with the updated amount.
        """
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA['orders_recurring'].get('update_orderrecurring_status')
        status_dict = {'status': status}
        res = self.client.patch(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/orderrecurring/%s/' % (self.base_url, orderrecurring_id),
            json=status_dict)
        return {
            'res': res,
            'success': (200 < res.status_code < 400)
        }

    def test_service_get_orders_recurring(self, data):
        r = requests.Response()
        if data == None:
            r.orders_recurring = []
            r.status_code = 404
        else:
            r.status_code = 200
            r.orders_recurring = data['user']['orders']
        return r

    def test_service_get_order_recurring(self, order_recurring, order):
        r = requests.Response()
        if order_recurring == None:
            r.order_recurring = {}
            r.status_code = 404
        else:
            r.status_code = 200
            order_recurring['order'] = order
            r.data = order_recurring
        return r
