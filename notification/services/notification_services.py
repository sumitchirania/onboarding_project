import logging

from ..models.notification import Notification

logger = logging.getLogger(__name__)


class NotificationService:

    def get_notifications(self):
        return Notification.objects.all()

    def create_notification(self, data):
        return Notification.objects.create(**data)

