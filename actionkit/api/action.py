import json
import re
import requests

from actionkit.api import base
from actionkit.api.test_data import TEST_DATA

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
                res = self.test_service_post(TEST_DATA['actions'][action_url])
            else:
                res = self.test_service_post(None)
            return {'res': res, 'fields': res.action}
        if action_url:
            result = self.client.get('%s%s' % (self.base_url, action_url))

            if result.status_code == 200:
                return result.json()
        elif action_id:
            result = self.client.get(
                '%s/rest/v1/action/%s' % (self.base_url, action_id),
                )
            if result.status_code == 200:
                return result.json()

    def update_action(self, action_id, update_dict):
        if getattr(self.settings, 'AK_TEST', False):
            if str(action_id) in TEST_DATA['actions']:
                res = self.test_service_post(TEST_DATA['actions'][str(action_id)])
            else:
                res = self.test_service_post(None)
            return {'res': res, 'action': res.action}

        # Get the action by its ID
        get_response = self.client.get(
            '%s/rest/v1/action/%s/' % (self.base_url, action_id)
        )
        resource_uri = get_response.json()['resource_uri']
        response = self.client.patch(
            '%s%s' % (self.base_url, resource_uri),
            data=json.dumps({'fields': update_dict})
        )
        return self._http_return(response)

    def test_service_post(self, data):
        r = requests.Response()
        if data == None:
            r.action = {}
            r.status_code = 404
        else:
            r.status_code = 200
            r.action = data['action']
        return r
