import csv
import json
import re
import requests
import sys
try:
    from six import StringIO
except ImportError:
    from io import StringIO

from actionkit.api import base


class AKUserAPI(base.ActionKitAPI):

    def set_usertag(self, user_id, name_or_dict, value=None):
        """
        send a dict, or a single name, value pair
        """
        if not hasattr(name_or_dict, 'get') and value:
            name_or_dict = { name_or_dict: value}

        res = self.client.patch(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/user/%s/' % (self.base_url, user_id),
            data=json.dumps({ 'fields': name_or_dict }))
        return self._http_return(res)

    def add_allowed_usertag(self, userfield_name):
        res = self.client.post(
            '%s/rest/v1/alloweduserfield/' % self.base_url,
            json={'name': userfield_name})
        return self._http_return(res)

    def create_user(self, user_dict):
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get(user_dict.get('email', 'create_user'))
        res = self.client.post(
            '%s/rest/v1/user/' % self.base_url,
            json=user_dict)
        rv = {'res': res}
        if res.headers.get('Location'):
            rv['id'] = re.findall(r'(\d+)/$', res.headers['Location'])[0]
        return rv

    def get_user(self, user_id):
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get(user_id)
        res = self.client.get(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/user/%s/' % (self.base_url, user_id))
        return {'res': res,
                'user': res.json() if res.status_code == 200 else None}

    def update_user(self, user_id, update_dict):
        res = self.client.patch(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/user/%s/' % (self.base_url, user_id),
            data=json.dumps(update_dict))
        return self._http_return(res)

    def user_search(self, query_params={}):
        res = ''
        search_string = '?'
        search_array = []
        res = self.client.get('%s/rest/v1/user/' % (self.base_url), params=query_params)
        return {'res': res, 'users': res.json() if res.status_code == 200 else None}

    def add_phone(self, user_id, phone, phone_type):
        res = self.client.post('%s/rest/v1/phone/' % (self.base_url), json={'user': user_id, 'phone_type': phone_type, 'phone': phone})
        return {'res': res, phone: res.json() if res.status_code == 200 else None}

    def get_phone(self, phone_id=None, url=None):
        assert(phone_id or url)
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get(url)
        if not url:
            #the '/' at the end is IMPORTANT!
            url = '/rest/v1/phone/%s/' % phone_id
        res = self.client.get(
            '%s%s' % (self.base_url, url))
        return {'res': res,
                'phone': res.json() if res.status_code == 200 else None}

    def update_phone(self, phone_id, update_dict):
        if 'delete' in update_dict:
            res = self.client.delete(
                '%s/rest/v1/phone/%s/' % (self.base_url, phone_id))
            return {'res': res}
            # return self._http_return(res)
            # res = delete_phone(phone_id)
            # return self._http_return(res)
        else:
            res = self.client.patch(
                #the '/' at the end is IMPORTANT!
                '%s/rest/v1/phone/%s/' % (self.base_url, phone_id),
                data=json.dumps(update_dict))
            return {'res': res, 'phone': res.json() if res.status_code == 200 else None}
            # return self._http_return(res)

    def login_token(self, user_id, ttl=86400):
        res = self.client.post(
            '{}/rest/v1/user/{}/logintoken/'.format(self.base_url, user_id),
            data={'ttl': ttl})
        if res.status_code == 200:
            return res.json().get('token')
        else:
            return None

    def payment_token(self, bto_paymenttoken_id):
        res = self.client.get(
            '{}/rest/v1/paymenttoken/{}'.format(self.base_url, bto_paymenttoken_id))
        if res.status_code == 200:
            resjson = res.json()
            user_id = re.findall(r'/rest/v1/user/(\d+)', resjson["user"])
            return {
                "id": resjson["id"],
                "status": resjson["status"],
                "token_id": resjson["token_id"],
                "user_id": int(user_id[0]) if user_id else None,
                "res": res
            }
        else:
            return None

    def bulk_upload(self, import_page, csv_file, autocreate_user_fields=0):
        """
        Note: If you get a 500 error, try sending a much smaller file (say, one row),
        which is more likely to return the proper 400 with a useful error message
        """
        #base.py defaults to JSON, but this has to be form/multi-part....
        upload_client = self.get_client({'accepts': 'application/json'})
        res = upload_client.post(
            '%s/rest/v1/upload/' % self.base_url,
            files={'upload': csv_file},
            data={'page': import_page,
                  'autocreate_user_fields': int(autocreate_user_fields)})
        rv = {'res': res,
              'success': res.status_code == 201,
              'progress_url': res.headers.get('Location')}
        return rv

    def bulk_upload_rows(self, import_page, headers, rows, autocreate_user_fields=0):
        csv_file = StringIO()
        outcsv = csv.writer(csv_file)

        outcsv.writerow(headers)
        if sys.version_info.major >= 3:
            outcsv.writerows(rows)
        else: #this is the nightmare python3 has saved us from:
            for row in rows:
                outcsv.writerow([(s.encode("utf-8") if isinstance(s, unicode) else s)
                                 for s in row])
        return self.bulk_upload(import_page, StringIO(csv_file.getvalue()),
                                autocreate_user_fields=autocreate_user_fields)


TEST_DATA = {
    'create_user': {
        'res': None,
        'id': 123123,
    },
    'example@example.com': {
        'res': None,
        'id': 123123,
    },
    '/rest/v1/phone/8675309/': {
        'res': None,
        'phone': {
            "created_at": "2015-11-24T21:07:58",
            "id": 8675309,
            "normalized_phone": "5558675309",
            "phone": "5558675309",
            "resource_uri": "/rest/v1/phone/8675309/",
            "source": "user",
            "type": "home",
            "updated_at": "2016-03-29T16:41:10",
            "user": "/rest/v1/user/123123/"
        }
    },
    '123123': { #fake userid
        'res': None,
         #some fields removed for brevity.
         # add them back if you need them for testing
        'user': {
            "address1": "123 Main St.",
            "address2": "",
            "city": "Cleveland",
            "country": "United States",
            "created_at": "2015-11-18T16:22:31",
            "email": "example@example.com",
            "fields": { },
            "first_name": "Roger",
            "last_name": "AndMe",
            "id": 123123,
            "phones": [
                "/rest/v1/phone/8675309/"
            ],
            "postal": "44123",
            "region": "OH",
            "state": "OH",
            "updated_at": "2016-07-11T18:19:26",
            "zip": "44123",
        }
    }
}
