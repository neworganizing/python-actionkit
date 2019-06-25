import json
import re
import requests
import sys

from actionkit.api.base import ActionKitAPI

class AKMailingAPI(ActionKitAPI):

    def update_mailing(self, mailing_id, update_dict):
        res = self.client.patch(
            #the '/' at the end is IMPORTANT!
            '%s/rest/v1/mailing/%s/' % (self.base_url, mailing_id),
            data=json.dumps(update_dict))
        return self._http_return(res)

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
                'mailings': res.json()['objects'] if res.status_code == 200 else None
               }

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
        }
    }




