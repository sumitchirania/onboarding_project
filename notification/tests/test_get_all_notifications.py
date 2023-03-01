from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models.notification import Notification
from ..serializers.notifications_serializer import NotificationSerializer


# initialize the APIClient app
client = Client()


class GetAllNotificationsTest(TestCase):
    """ Test module for GET all notifications API """

    notification_dummy_data_1 = {'title': 'Hey Newbie', 'desc': 'Get Flat 25% Off on First Purchase'}
    notification_dummy_data_2 = {'title': 'Hello', 'desc': 'Get Flat 20% Off on First Purchase'}

    def setUp(self):
        Notification.objects.create(**GetAllNotificationsTest.notification_dummy_data_1)
        Notification.objects.create(**GetAllNotificationsTest.notification_dummy_data_2)

    def test_get_all_notifications(self):
        # get API response
        response = client.get(reverse('notifications'))
        expected_keys = [
            'id', 'title', 'desc'
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(expected_keys).issubset(response.data[0].keys()), True)
        self.assertEqual(isinstance(response.data, list), True)

