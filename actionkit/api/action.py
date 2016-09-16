import json
import re
import requests

from actionkit.api import base

class AKActionAPI(base.ActionKitAPI):

    def create_action(self, akid, page, fields=None):
        data = {
            'akid': akid,
            'page': page
        }
        if fields is not None:
            data.update(fields)

        result = self.client.post(
            '%s/rest/v1/action/' % self.base_url,
            data=json.dumps(data)
        )

        return {'res': result}
