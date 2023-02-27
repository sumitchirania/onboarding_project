import logging

from ..models.subscriber import Subscriber

logger = logging.getLogger(__name__)


class SubscriberService(object):

    def __int__(self):
        pass

    def get_subscribers_list(self):
        return Subscriber.objects.all()

    def create_subscriber(self, data):
        return Subscriber.objects.create(**data)

