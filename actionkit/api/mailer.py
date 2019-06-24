import json
import re
import requests
import sys
import time

from actionkit.api.base import ActionKitAPI

try:
    import urllib.parse
    encode_url = urllib.parse.urlencode
except ImportError:
    # python2
    import urllib
    encode_url = urllib.urlencode

class AKMailerAPI(ActionKitAPI):

    """
        Manages mailing build and send. For mailing content CRUD use mailing.py.
    """

    def copy_mailing(self, mailing_id):
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get('copy_mailing')
        res = self.client.post(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/mailer/%s/copy/' % (self.base_url, mailing_id)
            )
        if res.status_code == 201:
            rv = {'res': res}
            if res.headers.get('Location'):
                rv['id'] = re.findall(r'(\d+)/$', res.headers['Location'])[0]
            return rv
        else:
            return None

    def rebuild_mailing(self, mailing_id):
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get('rebuild_mailing')
        res = self.client.post(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/mailer/%s/rebuild/' % (self.base_url, mailing_id),
            )
        if res.status_code == 201:
            rv = {'res': res}
            if res.headers.get('Location'):
                rv['status'] = res.headers.get('Location')
            return rv
        else:
            return None

    def get_rebuild_status(self, rebuild_status_url):
        """
            Rebuild_status_url is returned as 'status' from rebuild_mailing(). 
        """
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get('get_rebuild_status')
        res = self.client.get(rebuild_status_url) 
        if res.status_code == 200:
            res_dict = json.loads(res.text)
            rv = {'res': res}
            rv['finished'] = res_dict.get('finished', None)
            rv['finished_at'] = res_dict.get('finished_at', None)
            rv['target_count'] = res_dict.get('results', None)
            return rv
        else:
            return None

    def queue_mailing(self, mailing_id):
        """
            If the mailing has a scheduled_for field, it will send then; 
            otherwise it will send immediately. Returns URI to poll for send
            status in "location".

        """
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get('queue_mailing')
        res = self.client.post(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/mailer/%s/queue/' % (self.base_url, mailing_id),
            )
        if res.status_code == 201:
            rv = {'res': res}
            if res.headers.get('Location'):
                rv['status'] = res.headers.get('Location')
        return rv

    def get_queue_status(self, mailing_id):
        """
            Queue status updates every 10 seconds or slower.
        """
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get('get_queue_status')
        res = self.client.get(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/mailer/%s/progress/' % (self.base_url, mailing_id),
            )
        if res.status_code == 200:
            res_dict = json.loads(res.text)
            rv = {'res': res}
            rv['status'] = res_dict.get('status', None)
            rv['finished'] = res_dict.get('finished', None)
            rv['progress'] = res_dict.get('progress', None)
            rv['target_count'] = res_dict.get('expected_send_count', None)
            rv['started_at'] = res_dict.get('started_at', None)
            return rv
        else:
            return None

    def stop_mailing(self, mailing_id):
        """
            Moves a scheduled or sending mailing to draft status.
            Returns a status URL that can be used to confirm draft status
            after at least 10 seconds.
        """
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get('queue_mailing')
        res = self.client.post(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/mailer/%s/stop/' % (self.base_url, mailing_id)
            )
        if res.status_code == 202:
            rv = {'res': res}
            rv['status'] = '%s/rest/v1/mailer/%s/progress/' % (self.base_url, mailing_id)
            return rv 
        else:
            return None



    TEST_DATA = {
        'copy_mailing': {
            'res': None,
            'id': '1235'
        },
        'rebuild_mailing': {
            'res': None, 
            'status': 'https://act.example.org/rest/v1/mailer/1235/rebuild/status/1234/'
        },
        'poll_rebuild_status': {
            'res': None,
            'finished': True, 
            'finished_at': '2019-06-24T21:49:08', 
            'target_count': 1742
        },
        'queue_mailing': {
            'res': None,
            'status': 'https://act.example.org/rest/v1/mailer/1235/progress/'
        },
        'get_queue_status': {
            'res': None, 
            'status': 'scheduled', 
            'finished': False, 
            'progress': None, 
            'target_count': 1742, 
            'started_at': None
        }
    }




