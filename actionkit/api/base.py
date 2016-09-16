import requests

class ActionKitAPI(object):

    def __init__(self, settings):
        self.settings = settings
        self.client = requests.Session()
        self.client.auth = (settings.AK_USER, settings.AK_PASSWORD)
        self.client.headers.update({'content-type': 'application/json',
                                    'accepts': 'application/json'})

        self.base_url = settings.AK_BASEURL


    def _http_return(self, res):
        """
        Return based on http response success
        """
        #if 200 >= res.status_code < 300:
        return res

