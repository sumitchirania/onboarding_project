import json

from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


class CreateNotificationsTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        self.client = Client()
        self.notification_valid_dummy_data = {
            'title': 'Welcome',
            'desc': 'Flat 15% Off on your first order as a welcome gift'
        }
        self.notification_invalid_dummy_data = {
            'title': '',
            'desc': 'some_description'
        }

    def test_create_valid_notification(self):
        # get API response
        response = self.client.post(
            reverse('notifications'),
            data=json.dumps(self.notification_valid_dummy_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_notification(self):
        # get API response
        response = self.client.post(
            reverse('notifications'),
            data=json.dumps(self.notification_invalid_dummy_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
