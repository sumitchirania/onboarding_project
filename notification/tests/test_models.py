from django.test import TestCase
from ..models.notification import Notification


class NotificationTest(TestCase):
    """ Test module for notification model """

    first_test = {'title': 'Flat 10% Off', 'desc': 'Get Flat 10% Off on your first purchase.'}
    second_test = {'title': 'Flat 20% Off', 'desc': 'Get Flat 20% Off on your first purchase.'}

    def setUp(self):
        Notification.objects.create(**NotificationTest.first_test)
        Notification.objects.create(**NotificationTest.second_test)

    def test_notification(self):
        notification_10 = Notification.objects.get(title='Flat 10% Off')
        notification_20 = Notification.objects.get(title='Flat 20% Off')
        print('Running Notification Model tests')
        self.assertEqual(
            notification_10.desc, "Get Flat 10% Off on your first purchase.")
        self.assertEqual(
            notification_20.desc, "Get Flat 20% Off on your first purchase.")

