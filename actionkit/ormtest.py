import sys
import inspect

import django

'''
A very non-standard ORM tester
Must be run from a django shell (python manage.py shell) and have a database
named 'actionkit' in your DATABASES.
'''

def test_django_orm():
    result = []
    for name, obj in inspect.getmembers(sys.modules['actionkit.models']):
        if type(obj) == django.db.models.base.ModelBase and name != '_akit_model':
            print "Testing %s" % name
            all = obj.objects.using('actionkit').select_related().all()
            result += list(all[:1])