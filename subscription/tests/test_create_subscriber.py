import json

from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


# initialize the APIClient app
client = Client()


class CreateSubscribersTest(TestCase):
    """ Test module for create a subscriber API """

    subscriber_valid_dummy_data = {'endpoint': 'www.subscriber1.com', 'public_key': 'some_public_key',
                                   'auth_key': 'some_auth_key', 'name': 'subscriber1'}
    subscriber_invalid_dummy_data = {'endpoint': '', 'public_key': 'some_public_key',
                                     'auth_key': 'some_auth_key', 'name': 'subscriber2'}

    def setUp(self):
        pass

    def test_create_valid_subscriber(self):
        # get API response
        response = client.post(
            reverse('subscriber'),
            data=json.dumps(CreateSubscribersTest.subscriber_valid_dummy_data),
            content_type='application/json'
        )
        print('creating a valid subscriber test')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_subscriber(self):
        # get API response
        response = client.post(
            reverse('subscriber'),
            data=json.dumps(CreateSubscribersTest.subscriber_invalid_dummy_data),
            content_type='application/json'
        )
        print('creating an invalid subscriber test')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
