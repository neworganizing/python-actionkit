from actionkit.api.base import ActionKitAPI

from urllib.parse import urlencode

class AKOrderRecurringAPI(ActionKitAPI):

    def get_orderrecurring_detail(self, orderrecurring_id):
        """
            Get recurring donation info and billing info
        """
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get('get_orderrecurring_detail')
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
            return TEST_DATA.get('list_orderrecurring')
        if user_id:
            result = self.client.get(
                '%s/rest/v1/orderrecurring/?user=%s&%s' % (
                    self.base_url, user_id, urlencode(query_params)))
        else:
            result = self.client.get(
                '%s/rest/v1/orderrecurring/?%s' % (
                    self.base_url, urlencode(query_params)))
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
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get('update_orderrecurring_status')
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
TEST_DATA = {
    "get_orderrecurring_detail": {
        'res': None,
        "account": "Test Account",
        "action":"/rest/v1/donationaction/999999226/",
        "amount":"1.12",
        "amount_converted":"1.12",
        "card_num":"1111",
        "created_at":"2020-04-23T20:42:55",
        "currency":"USD",
        "exp_date":"0822",
        "id":999114,
        "order":{
            "account":"MoveOn.org Political Action",
            "action":"/rest/v1/donationaction/999999226/",
            "card_num_last_four":"3676",
            "created_at":"2020-04-23T20:42:55",
            "currency":"USD",
            "id":99999527,
            "import_id":"None",
            "orderdetails":[

            ],
            "orderrecurrings":[
                "/rest/v1/orderrecurring/999114/"
            ],
            "payment_method":"cc",
            "resource_uri":"/rest/v1/order/99999527/",
            "reverse":"/rest/v1/order/99999527/reverse/",
            "shipping_address":"None",
            "status":"completed",
            "total":"1.12",
            "total_converted":"1.12",
            "transactions":[
                "/rest/v1/transaction/99999745/",
                "/rest/v1/transaction/99999746/",
                "/rest/v1/transaction/99999830/"
            ],
            "updated_at":"2020-04-23T20:42:59",
            "user":"/rest/v1/user/99999835/",
            "user_detail":"/rest/v1/orderuserdetail/99999000/"
        },
        "period":"months",
        "recurring_id":"z9zzzz",
        "resource_uri":"/rest/v1/orderrecurring/999114/",
        "start":"2020-05-23",
        "status":"canceled_by_admin",
        "updated_at":"2020-04-23T23:02:39",
        "user":"/rest/v1/user/99999835/",
        "user_detail":{
            "address1":"123 Main St",
            "address2":"",
            "city":"Any City",
            "country":"United States",
            "created_at":"2020-04-23T20:42:55",
            "email":"test@example.com",
            "first_name":"Testy",
            "id":99999000,
            "last_name":"Test",
            "middle_name":"",
            "orders":[
                "/rest/v1/order/99999527/"
            ],
            "plus4":"4052",
            "postal":"99999-4052",
            "prefix":"",
            "region":"AZ",
            "resource_uri":"/rest/v1/orderuserdetail/99999000/",
            "source":"",
            "state":"AZ",
            "suffix":"",
            "updated_at":"2020-04-23T20:42:55",
            "zip":"99999"
        }
    },
    "list_orderrecurring": {
        "res": None,
        "objects":[
            {
                "account":"Test Account",
                "action":"/rest/v1/donationaction/999999226/",
                "amount":"1.12",
                "amount_converted":"1.12",
                "card_num":"1111",
                "created_at":"2020-04-23T20:42:55",
                "currency":"USD",
                "exp_date":"0822",
                "id":999114,
                "order":"/rest/v1/order/99999527/",
                "period":"months",
                "recurring_id":"z9zzzz",
                "resource_uri":"/rest/v1/orderrecurring/999114/",
                "start":"2020-05-23",
                "status":"canceled_by_admin",
                "updated_at":"2020-04-23T23:02:39",
                "user":"/rest/v1/user/99999835/"
            }
        ]
    },
    "update_orderrecurring_status": {
        'res': None,
        'success': True
    }

}
