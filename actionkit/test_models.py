from django.test import TestCase
from actionkit.models import CoreUser, CoreUnsubscribeaction


class UserTestCase(TestCase):
    def test_actionfield(self):
        queryset = CoreUser.objects.all()
        queryset = CoreUser.objects.actionfield_filter(
            queryset, 'signon_petition_id',
            pages=[2202, 2203],
            min_count=5,
            since_days=5
        )
        results = list(queryset)
        self.assertEqual(results, [])
