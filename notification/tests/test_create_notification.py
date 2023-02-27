import json

from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


# initialize the APIClient app
client = Client()


class CreateNotificationsTest(TestCase):
    """ Test module for GET all puppies API """

    notification_valid_dummy_data = {'title': 'Welcome', 'desc': 'Flat 15% Off on your first order as a welcome gift'}
    subscriber_invalid_dummy_data = {'title': '', 'desc': 'some_description'}

    def setUp(self):
        pass

    def test_create_valid_notification(self):
        # get API response
        response = client.post(
            reverse('notification'),
            data=json.dumps(CreateNotificationsTest.notification_valid_dummy_data),
            content_type='application/json'
        )
        print('creating a valid notification test')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_notification(self):
        # get API response
        response = client.post(
            reverse('notification'),
            data=json.dumps(CreateNotificationsTest.subscriber_invalid_dummy_data),
            content_type='application/json'
        )
        print('creating an invalid notification test')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
