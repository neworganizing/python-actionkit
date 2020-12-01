import json

from actionkit.api import base

class AKUserfieldAPI(base.ActionKitAPI):
  def update_userfield(self, userfield_id, update_dict):
    res = self.client.put(
      #the '/' at the end is IMPORTANT!
      '%s/rest/v1/userfield/%s/' % (self.base_url, userfield_id),
      data=json.dumps(update_dict))
    return self._http_return(res)