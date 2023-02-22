import logging

from ..models.subscriber import Subscriber

logger = logging.getLogger(__name__)


class SubscriberCrud(object):

    def __int__(self):
        pass

    def create_subscriber(self, data):
        print(data, 'data')
        success = False
        try:
            Subscriber.objects.create(**data)
            success = True
        except Exception as e:
            logger.error(e, exc_info=True)
        return success
