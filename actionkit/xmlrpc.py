import xmlrpc.client as xmlrpc

from actionkit.errors import ActionKitGeneralError

class ActionKitXML(xmlrpc.ServerProxy, object):
    def __init__(self, **kwargs):
        if 'instance' not in kwargs:
            raise ActionKitGeneralError("No Instance Provided")

        self.ak_instance = kwargs['instance']

        if ('username' and 'password') not in kwargs:
             raise ActionKitGeneralError("No Username and or Password Provided")

        self.ak_user = kwargs['username']
        password = kwargs['password']
        url = "https://{user}:{password}@{instance}/api/".format(user=self.ak_user,password=password,instance=self.ak_instance)

        super(ActionKitXML, self).__init__(url)
