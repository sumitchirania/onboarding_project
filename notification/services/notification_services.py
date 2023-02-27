import logging

from ..models.notification import Notification

logger = logging.getLogger(__name__)


class NotificationServices(object):

    def __int__(self):
        pass

    def get_notifications_list(self):
        return Notification.objects.all()

    def create_notification(self, data):
        return Notification.objects.create(**data)

