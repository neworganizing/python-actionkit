****************
python-actionkit
****************

python-actionkit is a python wrapper/sdk allowing easy access to the REST, XMLRPC and SQL interfaces to the `ActionKit CRM`_.

.. _ActionKit CRM: http://www.actionkit.com/

REST Interface
--------------

ActionKit provides a `REST Interface`_ based on `Tastypie`_. It allows connectivity as an authenticated user both using username/password authentication as well as username/api-key authentication. It also allows a limited number of actions to be taken as guest users. 

python-actionkit interacts with the REST interface viw the requests library

To initialize a connection using the login/password::

    from actionkit import ActionKit
    ak = ActionKit(instance='act.yourdomain.com', username='yourusername', password='abcd123')

To use the API key authentication use::

    from actionkit import ActionKit
    ak = ActionKit(instance='act.yourdomain.com', username='yourusername', api_key='abcd123123123')


To use guest access, use::

    from actionkit import ActionKit
    ak = ActionKit(instance='act.yourdomain.com')

Accessing individual resources is easy. If you wanted a dictionary of the JSON response ActionKit returns when you request the ``user`` with the ID of 1, you'd use::

    user1 = ak.user.get(1)

To update that record (using a ``PUT`` request), simply pass in the ID as an argument and then the updated record::

    result = ak.user.update(1, {'first_name': 'Joe'})

To delete that record (using a ``DELETE`` request), use::

    result = ak.user.delete(1)

ActionKit's REST interface also allows raw SQL access. To get the first record from the ``core_user`` table simply call the ``sql`` method::

    sql_result = ak.sql("SELECT * FROM core_user LIMIT 1")

.. _REST Interface: https://roboticdogs.actionkit.com/docs/manual/api/rest/index.html
.. _Tastypie: http://django-tastypie.readthedocs.org/en/latest/

XML-RPC
-------

ActionKit also has an `XML-RPC`_ API interface. Usually this is invoked by using the ``xmlrpc`` library, but python-actionkit provides a simple shortcut to get an xmlrpc ``ServerProxy`` object that is connected to ActionKit

To create a new ``ServerProxy`` to ActionKit, simply create a new ``ActionKitXML`` object::

    from actionkit import ActionKitXML
    akxml = ActionKitXML(instance='act.yourdomain.com', username='yourusername', password='abcd123')

Then to pull a dictionary containing the details from User #1 simply use the command::

    user1 = akxml.User.get({'id': 1})

.. _XML-RPC: https://roboticdogs.actionkit.com/docs/manual/api/

Django ORM
----------

ActionKit is based on Django 1.1 and conviently provides clients direct SQL access to a MySQL Slave. Taking advantage of these two things allows access to client data with minimal latency as well as considerable development speed advantages.

To pull a ``CoreUser`` object representing the user if the ID 1, first ensure that your actionkit database details are defined in your ``settings.py`` ``DATABASES`` dictionary, then request the CoreUser object using the id::

    from actionkit.models import CoreUser
    user1 = CoreUser.objects.using('actionkit').get(id=1)

All available models and their fields can be found in the ``models.py`` file contained in the `python-actionkit repository`_

.. _python-actionkit repository: https://github.com/neworganizing/python-actionkit

Authors & License
-----------------

This plugin was built in-house by the team at the `New Organizing Institute`_ led by `Nick Catalano`_ and is released under an open source Apache 2.0 license.

Models are based off the scheme extracted from the ActionKit database, developed by `We Also Walk Dogs`_

.. _New Organizing Institute: http://neworganizing.com/
.. _Nick Catalano: https://github.com/nickcatal
.. _We Also Walk Dogs: http://www.actionkit.com/