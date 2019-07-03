import json
import re
import requests
import sys

from actionkit.api.base import ActionKitAPI

class AKMailingAPI(ActionKitAPI):

    """
        CRUD, queue, stop and rebuild mailings.
    """

    def create_mailing(self, mailing_dict):
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get(mailing_dict.get('create_mailing'))
        res = self.client.post(
            '%s/rest/v1/mailing/' % self.base_url,
            json=mailing_dict)
        rv = {'res': res}
        if res.headers.get('Location'):
            rv['id'] = re.findall(r'(\d+)/$', res.headers['Location'])[0]
        return rv

    def get_mailings(self, mailing_id=False, params={}):
        if getattr(self.settings, 'AK_TEST', False):
                return TEST_DATA.get(mailing_id)
        if mailing_id:
            res = self.client.get(
                #the '/' at the end is IMPORTANT!
                '%s/rest/v1/mailing/%s/' % (self.base_url, mailing_id))
            return {'res': res,
                    'mailing': res.json() if res.status_code == 200 else None}
        elif params:
            res = self.client.get(
                #the '/' at the end is IMPORTANT!
                '%s/rest/v1/mailing/' % (self.base_url), params=params)
        else:
            res = self.client.get(
                '{}/rest/v1/mailing/'.format(self.base_url))
        return {'res': res,
                'mailings': res.json()['objects'] if res.status_code == 200 else None}

    def update_mailing(self, mailing_id, update_dict):
        res = self.client.patch(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/mailer/%s/' % (self.base_url, mailing_id),
            data=json.dumps(update_dict))
        return self._http_return(res)

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
            '%s/rest/v1/mailer/%s/rebuild/' % (self.base_url, mailing_id)
            )
        if res.status_code == 201:
            rv = {'res': res}
            if res.headers.get('Location'):
                rv['status_url'] = res.headers.get('Location')
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
            '%s/rest/v1/mailer/%s/queue/' % (self.base_url, mailing_id)
            )
        if res.status_code == 201:
            rv = {'res': res}
            if res.headers.get('Location'):
                rv['status_url'] = res.headers.get('Location')
        return rv

    def get_queue_status(self, mailing_id):
        """
            Queue status updates every 10 seconds or slower.
        """
        if getattr(self.settings, 'AK_TEST', False):
            return TEST_DATA.get('get_queue_status')
        res = self.client.get(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/mailer/%s/progress/' % (self.base_url, mailing_id)
            )
        if res.status_code == 200:
            res_dict = res.json()
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
            rv['status_url'] = '%s/rest/v1/mailer/%s/progress/' % (self.base_url, mailing_id)
            return rv 
        else:
            return None
    

    TEST_DATA = {
        'create_mailing': {
            'res': None,
            'id': '1234'
        },
        1234: {  
            'archive':'',
            'autotest_max_unsub_rate':None,
            'autotest_metric':None,
            'autotest_status':'default',
            'autotest_wait_minutes':None,
            'created_at':'2019-06-12T20:36:40',
            'custom_fromline':'',
            'errors':[],
            'exclude_ordering':1000,
            'excludes':'/rest/v1/mailingtargeting/129885/',
            'expected_send_count':3800458,
            'fields':{ },
            'finished_at':None,
            'fromline':{  
                'created_at':'2017-08-08T18:16:45',
                'from_line':'"Cat Person" <cat-person@example.com>',
                'hidden':False,
                'id':1234,
                'is_default':False,
                'resource_uri':'/rest/v1/fromline/1234/',
                'updated_at':'2019-02-01T18:34:37'
            },
            'hidden':False,
            'html':'<p>This email is about cats!</p>',
            'id':1234,
            'includes':'/rest/v1/mailingtargeting/1234/',
            'limit':None,
            'limit_percent':None,
            'mailingstats':'/rest/v1/mailingstats/1234/',
            'mails_per_second':None,
            'notes':'test_note',
            'pid':None,
            'progress':None,
            'query_completed_at':'2019-06-12T20:47:17',
            'query_previous_runtime':None,
            'query_queued_at':'2019-06-12T20:44:32',
            'query_started_at':'2019-06-12T20:44:35',
            'query_status':'saved',
            'query_task_id':'1234',
            'query_uuid':None,
            'queue_task_id':None,
            'queued_at':None,
            'rate':None,
            'rebuild_query_at_send':True,
            'recurring_schedule':None,
            'recurring_source_mailing':None,
            'reply_to':'',
            'requested_proof_date':None,
            'requested_proofs':5,
            'resource_uri':'/rest/v1/mailing/1234/',
            'scheduled_for':None,
            'send_date':'',
            'send_time_source':None,
            'send_time_validation_job':None,
            'sent_proofs':0,
            'sort_by':None,
            'started_at':None,
            'status':'model',
            'subjects':[  
                {  
                    'created_at':'2019-06-12T20:36:40',
                    'id':1234,
                    'mailing':'/rest/v1/mailing/1234/',
                    'preview_text':'',
                    'resource_uri':'/rest/v1/mailingsubject/1234/',
                    'text':'This email is about cats',
                    'updated_at':'2019-06-12T20:36:40'
                }
            ],
            'tags':[  
                '/rest/v1/tag/1234/',
                '/rest/v1/tag/1235/'
            ],
            'target_group_from_landing_page':False,
            'target_mergefile':False,
            'target_mergequery':False,
            'targeting_version':2,
            'targeting_version_saved':2,
            'test_remainder':None,
            'text':'',
            'updated_at':'2019-06-20T20:23:19',
            'use_autotest':False,
            'version':10,
            'web_viewable':False,
            'winning_subject':None
        },
        'copy_mailing': {
            'res': None,
            'id': '1235'
        },
        'rebuild_mailing': {
            'res': None, 
            'status_url': 'https://act.example.org/rest/v1/mailer/1235/rebuild/status/1234/'
        },
        'poll_rebuild_status': {
            'res': None,
            'finished': True, 
            'finished_at': '2019-06-24T21:49:08', 
            'target_count': 1742
        },
        'queue_mailing': {
            'res': None,
            'status_url': 'https://act.example.org/rest/v1/mailer/1235/progress/'
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





