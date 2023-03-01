from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models.subscriber import Subscriber
from ..serializers.subscribers_serializer import SubscriberSerializer


# initialize the APIClient app
client = Client()


class GetAllSubscribersTest(TestCase):
    """ Test module for GET all subscribers API """

    subscriber_dummy_data_1 = {'endpoint': 'www.subscriber1.com', 'public_key': 'some_public_key',
                               'auth_key': 'some_auth_key', 'name': 'subscriber1'}
    subscriber_dummy_data_2 = {'endpoint': 'www.subscriber2.com', 'public_key': 'some_public_key',
                               'auth_key': 'some_auth_key', 'name': 'subscriber2'}
    subscriber_dummy_data_3 = {'endpoint': 'www.subscriber3.com', 'public_key': 'some_public_key',
                               'auth_key': 'some_auth_key', 'name': 'subscriber3'}
    subscriber_dummy_data_4 = {'endpoint': 'www.subscriber4.com', 'public_key': 'some_public_key',
                               'auth_key': 'some_auth_key', 'name': 'subscriber4'}

    def setUp(self):
        Subscriber.objects.create(**GetAllSubscribersTest.subscriber_dummy_data_1)
        Subscriber.objects.create(**GetAllSubscribersTest.subscriber_dummy_data_2)
        Subscriber.objects.create(**GetAllSubscribersTest.subscriber_dummy_data_3)
        Subscriber.objects.create(**GetAllSubscribersTest.subscriber_dummy_data_4)

    def test_get_all_subscribers(self):
        # get API response
        response = client.get(reverse('subscribers'))
        expected_keys = [
            'id', 'endpoint', 'public_key', 'auth_key', 'name', 'email', 'is_active'
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(expected_keys).issubset(response.data[0].keys()), True)
        self.assertEqual(isinstance(response.data, list), True)

