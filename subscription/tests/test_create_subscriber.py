import json

from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


class CreateSubscribersTest(TestCase):
    """ Test module for create a subscriber API """

    def setUp(self):
        self.client = Client()
        self.subscriber_valid_dummy_data = {
            'endpoint': 'www.subscriber1.com', 'public_key': 'some_public_key',
            'auth_key': 'some_auth_key', 'name': 'subscriber1'
        }
        self.subscriber_invalid_dummy_data = {
            'endpoint': '', 'public_key': 'some_public_key',
            'auth_key': 'some_auth_key', 'name': 'subscriber2'
        }

    def test_create_valid_subscriber(self):
        # get API response
        response = self.client.post(
            reverse('subscribers'),
            data=json.dumps(self.subscriber_valid_dummy_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_subscriber(self):
        # get API response
        response = self.client.post(
            reverse('subscribers'),
            data=json.dumps(self.subscriber_invalid_dummy_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
