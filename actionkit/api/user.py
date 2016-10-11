import json
import re
import requests

from actionkit.api import base


class AKUserAPI(base.ActionKitAPI):

    def set_usertag(self, user_id, name_or_dict, value=None):
        """
        send a dict, or a single name, value pair
        """
        if not hasattr(name_or_dict, 'get') and value:
            name_or_dict = { name_or_dict: value}

        res = self.client.put(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/user/%s/' % (self.base_url, user_id),
            data=json.dumps({ 'fields': name_or_dict }))
        return self._http_return(res)

    def set_eventfield(self, event_id, name, value, eventfield_id=None):
        """
        send a dict, or a single name, value pair
        """
        d = { 'name': name,
              'value': value,
              'event': '/rest/v1/event/%s/' % event_id}
        method = 'post'
        #the '/' at the end is IMPORTANT!
        url = '%s/rest/v1/eventfield/' % self.base_url
        if eventfield_id:
            method = 'put'
            url = url + ('%s/' % eventfield_id)
        res = getattr(self.client, method)(url, data=json.dumps(d))
        #import pdb; pdb.set_trace()
        return self._http_return(res)

    def add_allowed_usertag(self, userfield_name):
        res = self.client.post(
            '%s/rest/v1/alloweduserfield/' % self.base_url,
            json={'name': userfield_name})
        return self._http_return(res)

    def get_user(self, user_id):
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get(user_id)
        res = self.client.get(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/user/%s/' % (self.base_url, user_id))
        return {'res': res,
                'user': res.json() if res.status_code == 200 else None}

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

    def add_phone(self, phone_dict):
        res = self.client.post(
            '%s/rest/v1/phone/' % self.base_url,
            json=phone_dict)
        rv = {'res': res}
        if res.headers.get('Location'):
            rv['id'] = re.findall(r'(\d+)/$', res.headers['Location'])[0]
        return rv

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
