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
        response = client.get(reverse('notification'))
        # get data from db
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
