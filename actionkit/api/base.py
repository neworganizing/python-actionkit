import requests
# modded this to let me send test or prod creds. not sure if this is the right approach. TKTK
class ActionKitAPI(object):

    def __init__(self, settings):
        self.settings = settings
        self.client = self.get_client({
            'content-type': 'application/json',
            'accepts': 'application/json'})

        self.base_url = settings.AK_BASEURL

        self.secret = getattr(settings, 'AK_SECRET', None)

    def get_client(self, default_headers={}):
        client = requests.Session()
        client.auth = (self.settings.AK_USER, self.settings.AK_PASSWORD)
        client.headers.update(default_headers)
        return client

    def _http_return(self, res):
        """
        Return based on http response success
        """
        #if 200 >= res.status_code < 300:
        return res
