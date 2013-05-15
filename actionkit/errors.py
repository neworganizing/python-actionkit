class ActionKitMoreThanOneRecord(Exception):
    '''
    Error Code: 300
    The value returned when an external ID exists in more than one record. The
    response body contains the list of matching records.
    '''
    pass


class ActionKitMalformedRequest(Exception):
    '''
    Error Code: 400
    The request couldn't be understood, usually becaue the JSON or XML body contains an error.
    '''
    pass

class ActionKitUnauthorized(Exception):
    '''
    Error Code: 401
    Either the resource needs authentication or the authentication provided is wrong.
    '''
    pass

class ActionKitRefusedRequest(Exception):
    '''
    Error Code: 403
    The request has been refused. Verify that the logged-in user has
    appropriate permissions.
    '''
    pass


class ActionKitResourceNotFound(Exception):
    '''
    Error Code: 404
    The requested resource couldn't be found. Check the URI for errors, and
    verify that there are no sharing issues.
    '''
    pass

class ActionKitGeneralError(Exception):
    '''
    A non-specific ActionKit error.
    '''
    pass