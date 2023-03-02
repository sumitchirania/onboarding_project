import logging

from ..models.notification import Notification
from ..serializers.notifications_serializer import NotificationSerializer

logger = logging.getLogger(__name__)


class NotificationAPIService:

    def get_notification_data(self, notification_id):

        try:
            notification = Notification.objects.get(pk=notification_id)
            data = NotificationSerializer(notification).data
            return {
                'title': data.get('title', ''),
                'desc': data.get('desc', '')
            }
        except Notification.DoesNotExist:
            return {}

