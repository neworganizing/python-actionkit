import json
import re
import requests
from actionkit.api import base
from actionkit.api.action import AKActionAPI

class AKEventAPI(base.ActionKitAPI):

    def create_signup(self, user_id, event_id, page_id, role='attendee', status='active', fields=None):
        data = {
            'event': '/rest/v1/event/%s/' % event_id,
            'page': '/rest/v1/eventsignuppage/%s/' % page_id,
            'role': role,
            'status': status,
            'user': '/rest/v1/user/%s/' % user_id,
        }
        if fields is not None:
            data['fields'] = fields
        result = self.client.post(
            '%s/rest/v1/eventsignup/' % self.base_url,
            data=json.dumps(data)
        )
        return {'res': result}

    def update_signup(self, signup_id, user_id, event_id, page_id, role='attendee', status='active', fields=None):
        data = {
            'event': '/rest/v1/event/%s/' % event_id,
            'page': '/rest/v1/page/%s/' % page_id,
            'role': role,
            'status': status,
            'user': '/rest/v1/user/%s/' % user_id,
        }
        if fields is not None:
            data['fields'] = fields
        result = self.client.put(
            '%s/rest/v1/eventsignup/%s/' % (self.base_url, signup_id),
            data=json.dumps(data)
        )
        return {'res': result}
