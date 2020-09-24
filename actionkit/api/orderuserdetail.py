import json

from actionkit.api import base

class AKOrderuserdetailAPI(base.ActionKitAPI):
  def update_orderuserdetail(self, orderuserdetail_id, update_dict):
    res = self.client.patch(
      #the '/' at the end is IMPORTANT!
      '%s/rest/v1/orderuserdetail/%s/' % (self.base_url, orderuserdetail_id),
      data=json.dumps(update_dict))
    return self._http_return(res)