import requests
import json

from urlparse import urlparse
import urllib

from actionkit.errors import *


class ActionKit(object):
    def __init__(self, **kwargs):
        '''Initialize the instance with the given parameters.

        Available kwargs

        All Authentication Mechanisms & Guest Access:

        * instance -- The hostname of your ActionKit instance. Usually 'act.yourdomain.com'

        Password Authentication:

        * username -- the ActionKit username to use for authentication
        * password -- the password for the username

        API Token Authentication:

        * username -- the ActionKit username to use for authentication
        * api_key -- the API key for the username. This is usually found in the user's detail page

        Guest Access:

        For guest access all that is required is the instance/hostname

        Universal Kwargs:

        * version -- the ActionKit version to use. Defaults to v1

        '''
        self.version = kwargs.get('version', 'v1')

        if 'instance' not in kwargs:
            raise ActionKitGeneralError('No Instance Provided')

        self.ak_instance = kwargs['instance']

        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }

        if ('username' in kwargs) and ('password' in kwargs):
            self.auth = True
            self.auth_type = "user"
            authcode = "{username}:{password}".format(username=kwargs[
                                                      'username'], password=kwargs['password']).encode("base64").strip()
            authheader = "Basic {code}".format(code=authcode)
            self.headers.update({'Authorization': authheader})
        elif ('username' in kwargs) and ('api_key' in kwargs):
            self.auth = True
            self.auth_type = "key"
            authheader = "ApiKey {username}:{key}".format(
                username=kwargs['username'], key=kwargs['api_key'])
            self.headers.update({'Authorization': authheader})
        else:
            self.auth = False
            self.auth_type = "guest"

        self.base_url = "https://{instance}/rest/{version}/".format(
            instance=self.ak_instance, version=self.version)

    def __getattr__(self, name):
        return AKResource(name, self.ak_instance, self.headers, self.version)

    def _call_actionkit(self, method, url, **kwargs):
        '''Utility method for performing HTTP call to ActionKit.

        Returns a `requests.result` object.
        '''
        result = requests.request(method, url, headers=self.headers, **kwargs)

        if result.status_code >= 300:
            _exception_handler(result)

        return result

    def raw(self, method, path, **kwargs):
        url = "https://{instance}{path}".format(
            instance=self.ak_instance, path=path)
        return self._call_actionkit(method, url, **kwargs)

    def get(self, path, **kwargs):
        return self.raw('GET', path, **kwargs).json()

    def post(self, path, **kwargs):
        return self.raw('POST', path, **kwargs).json()

    def put(self, path, **kwargs):
        return self.raw('PUT', path, **kwargs).json()

    def sql(self, query, **kwargs):
        data = kwargs
        data.update({'query': query})
        url = self.base_url + 'report/run/sql/'

        result = self._call_actionkit('POST', url, data=json.dumps(data))

        return result.json()

    def run_report(self, report, **kwargs):
        '''Immediately run a specific report

        This command will return a report immediately (so it may take a bit of time)
        Pass the report name as the first argument and then use kwargs to pass in
        fields to the report

        Arguments:

        * report -- Name of the report

        '''
        data = kwargs
        url = '{base_url}report/run/{report_name}/'.format(
            base_url=self.base_url, report_name=report)

        result = self._call_actionkit('POST', url, data=json.dumps(data))

        return result.json()

    def run_bgreport(self, report, **kwargs):
        '''Queue a report then grab the results

        Nearly identical to the run_report method, this method will queue a report
        then immediately attempt to grab the result.

        This is most useful when you want to run a report that ActionKit feels is too intensive
        to be run in real-time.

        '''

        data = kwargs
        url = '{base_url}report/background/{report_name}/'.format(
            base_url=self.base_url, report_name=report)

        create_result = self._call_actionkit(
            'POST', url, allow_redirects=True, data=json.dumps(data))
        result = self._call_actionkit('GET', create_result.headers['Location'])

        return result.json()


class AKResource(object):
    def __init__(self, resource_name, instance, headers, version='v1'):
        ''' AKReporce is a stand-in for a specific type of resource (User, Action, Page, etc)
        and allows you to perform actions on that resource.
        '''

        self.resource_name = resource_name
        self.base_url = "https://{instance}/rest/{version}/{resource_name}/".format(
            instance=instance, version=version, resource_name=resource_name)
        self.headers = headers

    def _call_actionkit(self, method, url, **kwargs):
        '''Utility method for performing HTTP call to ActionKit.

        Returns a `requests.result` object.
        '''
        result = requests.request(method, url, headers=self.headers, **kwargs)

        if result.status_code >= 300:
            _exception_handler(result)

        return result

    def schema(self):
        '''Method that returns the schema for the object type

        Returns a dictionary of the JSON schema
        '''
        result = self._call_actionkit('GET', self.base_url + 'schema')
        return result.json()

    def get(self, id):
        '''Method that returns a dictionary of a single record

        Arguments:

        * id -- The ID/Primary Key of a record you wish to get

        '''
        result = self._call_actionkit('GET', self.base_url + str(id))
        return result.json()

    def list(self, **kwargs):
        '''Allows listing/finding of existing records

        The kwargs passed to list() translate directly into query strings

        To find 50 users who are in the state of Wisconsin or Illinois, offset by 50, you'd use this:

        ak.user.list(state__in=['WI','IL'],_offset=50, _limit=50)

        Which would send a GET request to /user/?state=WI&state=IL&_offset=50&_limit=50

        '''
        result = self._call_actionkit(
            'GET', self.base_url + '?' + urllib.urlencode(kwargs, True))
        return result.json()

    def create(self, data):
        '''Creates a new record

        Arguments:

        * data -- A dictionary of data you wish to associate with the new record

        '''
        result = self._call_actionkit(
            'POST', self.base_url, data=json.dumps(data))
        try:
            return result.json()
        except ValueError:
            return result.status_code

    def delete(self, id):
        '''Deletes a record

        Arguments:

        * id -- The ID/Primary Key of the record you wish to delete

        '''
        result = self._call_actionkit('DELETE', self.base_url + str(id))
        return result.status_code

    def update(self, id, data):
        '''Updates an existing ActionKit record

        Arguments:

        * id -- ID/Primary Key of the record you wish to update
        * data -- Dictionary of the data you wish to overwrite the existing record with

        '''
        result = self._call_actionkit(
            'PUT', self.base_url + str(id), data=json.dumps(data))
        return result.json()

def _exception_handler(result):
    ''' A handler that will return the correct exception based on the error
    thrown by ActionKit
    '''
    url = result.url
    try:
        response_content = result.json()
    except Exception:
        response_content = result.text

    if result.status_code == 300:
        message = "More than one record for {url}. Response content: {content}"
        message = message.format(url=url, content=response_content)
        raise ActionKitMoreThanOneRecord(message)
    elif result.status_code == 400:
        message = "Malformed request {url}. Response content: {content}"
        message = message.format(url=url, content=response_content)
        raise ActionKitMalformedRequest(message)
    elif result.status_code == 401:
        message = "Expired session for {url}. Response content: {content}"
        message = message.format(url=url, content=response_content)
        raise ActionKitUnauthorized(message)
    elif result.status_code == 404:
        message = 'Resource Not Found. Response content: {content}'
        message = message.format(content=response_content)
        raise ActionKitResourceNotFound(message)
    elif result.status_code == 405:
        message = "Method not allowed for url {url}. Resonse content: {content}"
        message = message.format(url=url, content=response_content)
        raise ActionKitRefusedRequest(message)
    else:
        message = 'Error Code {status}. Response content: {content}'
        message = message.format(status=result.status_code, content=response_content)
        raise ActionKitGeneralError(message)