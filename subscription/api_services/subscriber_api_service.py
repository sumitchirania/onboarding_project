import logging

from ..models.subscriber import Subscriber
from ..serializers.subscribers_serializer import SubscriberSerializer

logger = logging.getLogger(__name__)


class SubscriberAPIService:

    def get_all_active_subscribers(self):
        subscribers = Subscriber.objects.filter(is_active=True)
        return SubscriberSerializer(subscribers, many=True).data
