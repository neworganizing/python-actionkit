from actionkit.api.base import ActionKitAPI

try:
    import urllib.parse
    encode_url = urllib.parse.urlencode
except ImportError:
    # python2
    import urllib
    encode_url = urllib.urlencode


class AKOrderRecurringAPI(ActionKitAPI):

    def create_orderrecurring(self, orderrecurring_dict):
        """
            Not even sure this is possible yet
        """
        # if getattr(self.settings, 'AK_TEST', False):
        #     return TEST_DATA.get(orderrecurring_dict.get('create_orderrecurring'))
        # res = self.client.put(
        #     '%s/rest/v1/mailing/' % self.base_url,
        #     json=orderrecurring_dict)
        # import pdb; pdb.set_trace()
        # return res
        pass

    def get_orderrecurring_detail(self, orderrecurring_id):
        """
            Get recurring donation info and billing info
        """
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
        if user_id:
            result = self.client.get(
                '%s/rest/v1/orderrecurring/?user=%s&%s' % (
                    self.base_url, user_id, encode_url(query_params)))
        else:
            result = self.client.get(
                '%s/rest/v1/orderrecurring/?%s' % (
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
        status_dict = {'status': status}
        res = self.client.patch(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/orderrecurring/%s/' % (self.base_url, orderrecurring_id),
            json=status_dict)
        return {
            'res': res,
            'success': (200 < res.status_code < 400)
        }

# TODO: add test data
