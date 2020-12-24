import json
import re
import requests

from actionkit.api import base

class AKActionAPI(base.ActionKitAPI):

    def create_action(self, akid, page, fields=None):
        data = {
            'akid': akid,
            'page': page
        }
        # For custom fields, prefixed with action_
        if fields is not None:
            data.update(fields)

        result = self.client.post(
            '%s/rest/v1/action/' % self.base_url,
            data=json.dumps(data)
        )

        return {'res': result}

    def get_action(self, action_id=False, action_url=False):
        """
            Get order and billing info
        """
        if getattr(self.settings, 'AK_TEST', True):
            if action_url and str(action_url) in TEST_DATA['actions']:
                response = self.test_service_post(TEST_DATA['actions'][action_url])
            else:
                response = self.test_service_post(None)
            return {'response': response, 'action': response.action}
        if action_url:
            response = self.client.get('%s%s' % (self.base_url, action_url))
            return {'response': response, 'action': response.json()}
        elif action_id:
            response = self.client.get(
                '%s/rest/v1/action/%s' % (self.base_url, action_id),
                )

            return {'response': response, 'action': response.json()}

    def update_action(self, action_id, update_dict):
        if getattr(self.settings, 'AK_TEST', False):
            if str(action_id) in TEST_DATA:
                res = self.test_service_post(TEST_DATA[str(action_id)])
            else:
                res = self.test_service_post(None)
            return {'res': res, 'action': res.action}
        response = self.client.patch(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/action/%s/' % (self.base_url, action_id),
            data=json.dumps(update_dict))
        if response.status_code == 202:
            return "Successfully changed source to {0} on action #{1}".format(
                source,
                action_id
            )
        return self._http_return(response)

TEST_DATA = {
    '123123a': { #fake actionid
        'res': 200,
         #some fields removed for brevity.
         # add them back if you need them for testing
        'action': {
            'akid': '.401.-9Mop1',
            'created_at': '1999-10-13T17:07:00',
            'created_user': False,
            'fields': {},
            'id': 1,
            'ip_address': None,
            'is_forwarded': False,
            'link': None,
            'mailing': None,
            'opq_id': '',
            'page': '/rest/v1/importpage/12/',
            'referring_mailing': None,
            'referring_user': None,
            'resource_uri': '/rest/v1/importaction/1/',
            'source': 'initial_ak_import',
            'status': 'complete',
            'subscribed_user': False,
            'taf_emails_sent': None,
            'type': 'Import',
            'updated_at': '2015-09-23T02:21:30',
            'user': '/rest/v1/user/401/'
        }
    },
}
