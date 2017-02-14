import datetime
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

    def update_event_action(self, event_id, fields):
        #replicates what you would send to create_action
        eventfields = {}
        actionfields = {}
        dateinfo = {}
        for f,val in fields.items():
            if f.startswith('event_starts_at'):
                dateinfo[f] = val
            elif f.startswith('event_'):
                eventfields[f[len('event_'):]] = val
            elif f.startswith('action_'):
                actionfields[f[len('action_')]] = val
        if dateinfo:
            "2010-11-10T03:07:43"
            eventdate = datetime.datetime.strptime(
                '%s %s %s' % (
                    dateinfo.get('event_starts_at_date'),
                    dateinfo.get('event_starts_at_time'),
                    dateinfo.get('event_starts_at_ampm')
                ), '%m/%d/%Y %H:%M %p')
            eventfields['starts_at'] = eventdate.strftime('%Y-%m-%dT%H:%M:00')

        result = self.client.patch(
            '%s/rest/v1/event/%s/' % (self.base_url, event_id),
            json=eventfields)
        rv = {'res': result}
        if actionfields:
            fieldresults = []
            evt = self.get_event(event_id)
            cur_fields = dict([(f['name'], f) for f in evt['res'].json().get('fields', [])])
            for name,val in actionfields.items():
                if name in cur_fields:
                    if val != cur_fields[name]['value']:
                        fieldresults.append(self.set_event_field(event_id, name, val, cur_fields[name]['id']))
                else:
                    fieldresults.append(self.set_event_field(event_id, name, val))
            rv['fieldresults'] = fieldresults
        return rv

    def list_signups(self, user_id):
        def idfromurl(path):
            if '/' in path:
                return re.findall(r'/(\d+)/?$', path)[0]

        result = self.client.get(
            '%s/rest/v1/eventsignup/?user=%s' % (self.base_url, user_id))
        final_result = {'res': result}
        if result.status_code == 200:
            json = result.json()
            if json.get('objects'):
                for obj in json.get('objects'):
                    obj['event_id'] = idfromurl(obj.get('event'))
                    obj['page_id'] = idfromurl(obj.get('page'))
            final_result.update(json)
        return final_result

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

    def set_event_field(self, event_id, field_name, field_value, eventfield_id=None):
        d = { 'name': field_name,
              'value': field_value,
              'event': '/rest/v1/event/%s/' % event_id}
        method = 'post'
        #the '/' at the end is IMPORTANT!
        url = '%s/rest/v1/eventfield/' % self.base_url
        if eventfield_id:
            method = 'put'
            url = url + ('%s/' % eventfield_id)
        res = getattr(self.client, method)(url, json=d)
        return self._http_return(res)

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
