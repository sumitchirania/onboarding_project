import logging

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..services.push_service import PushService
from pywebpush import WebPushException

logger = logging.getLogger(__name__)


class PushNotificationView(APIView):

    def post(self, request):
        notification_id = request.data.get('notification_id', '')
        logger.info("Sending push notification to all subscribers for notification id {}".format(id))
        try:
            if notification_id:
                return PushService().send_notification_to_all_subscriber(notification_id=notification_id)
            else:
                return Response({"success": False, "msg": 'Invalid Notification id'}, status=status.HTTP_400_BAD_REQUEST)
        except WebPushException as e:
            logger.error("Attempt to send push-notification failed with exception={}".format(e))
            return Response({"success": False, "reason": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
