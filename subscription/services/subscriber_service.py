import logging

from ..models.subscriber import Subscriber

logger = logging.getLogger(__name__)


class SubscriberService:

    def get_subscribers(self):
        return Subscriber.objects.all()

    def create_subscriber(self, data):
        return Subscriber.objects.create(**data)

