from django.test import TestCase
from ..models.subscriber import Subscriber


class SubscriberTest(TestCase):
    """ Test module for Subscriber model """

    first_test = {'endpoint': 'www.pushowl.com', 'public_key': 'public_key',
                  'auth_key': 'auth_key', 'name': 'pushowl'}
    second_test = {'endpoint': 'www.sumit.com', 'public_key': 'public_key',
                   'auth_key': 'auth_key', 'name': 'sumit'}

    def setUp(self):
        Subscriber.objects.create(**SubscriberTest.first_test)
        Subscriber.objects.create(**SubscriberTest.second_test)

    def test_subscriber(self):
        subscriber_sumit = Subscriber.objects.get(name='sumit')
        subscriber_pushowl = Subscriber.objects.get(name='pushowl')
        print('Running Subscriber Model tests')
        self.assertEqual(
            subscriber_sumit.endpoint, "www.sumit.com")
        self.assertEqual(
            subscriber_pushowl.endpoint, "www.pushowl.com")

