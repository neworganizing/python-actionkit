import re
import requests
from actionkit.api import base
from actionkit.api.action import AKActionAPI

class AKEventAPI(base.ActionKitAPI):

    def get_event(self, event_id):
        result = self.client.get(
            '%s/rest/v1/event/%s' % (self.base_url, event_id)
        )
        return {'res': result}

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
            json=data
        )
        return {'res': result}

    def create_user_signup(self, event_id, page_name, fields):
        assert(fields.get('email') or fields.get('akid'))

        data = {
            'page': page_name,
            'event_id': event_id,
        }

        if fields:
            data.update(fields)
        result = requests.post('%s/rest/v1/action/' % self.base_url,
                               json=data)
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
            json=data
        )
        return {'res': result}

    def create_event_field(self, event_id, field_name, field_value):
        data = {
            'event': '/rest/v1/event/%s/' % event_id,
            'name': field_name,
            'value': field_value,
        }
        result = self.client.post(
            '%s/rest/v1/eventfield/' % self.base_url,
            json=data
        )
        return {'res': result}

    def get_event_fields(self, event_id=None, field_name=None, field_value=None):
        data = {}
        if event_id is not None:
            data['parent'] = '/rest/v1/event/%s/' % event_id
        if field_name is not None:
            data['name'] = field_name
        if field_value is not None:
            data['value'] = field_value
        result = self.client.get(
            '%s/rest/v1/eventfield/' % self.base_url,
            params=data
        )
        return {'res': result}

    def delete_event_field(self, eventfield_id):
        result = self.client.delete(
            '%s/rest/v1/eventfield/%s' % (self.base_url, eventfield_id)
        )
        return {'res': result}
