import logging

from rest_framework import status
from rest_framework.response import Response

from subscription.api_services.subscriber_api_service import SubscriberAPIService
from notification.api_services.notification_api_service import NotificationAPIService
from ..tasks.task_push_notification import task_send_notification

logger = logging.getLogger(__name__)


class PushService:

    def send_notification_to_all_subscriber(self, notification_id):
        notification_data = NotificationAPIService().get_notification_data(notification_id)
        if not notification_data:
            return Response({"success": False,
                             "msg": 'Notification not found for notification id {}'.format(notification_id)},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            subscribers = SubscriberAPIService().get_all_active_subscribers()
            for subscriber in subscribers:
                subscription_data = {
                    "endpoint": subscriber.endpoint,
                    "keys": {
                        "auth": subscriber.auth_key,
                        "p256dh": subscriber.public_key
                    }
                }
                task_send_notification.delay(subscription_data, notification_data)
        except Exception as e:
            print(e,'errror')
