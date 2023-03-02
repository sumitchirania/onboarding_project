import logging

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..services.push_service import PushService

logger = logging.getLogger(__name__)


class PushNotificationView(APIView):

    def post(self, request):
        print(request.data,'data')
        notification_id = request.data.get('notification_id', '')
        print(notification_id,'notification_id')
        logger.info("Sending push notification to all subscribers for notification id {}".format(id))
        if notification_id:
            return PushService().send_notification_to_all_subscriber(notification_id=notification_id)
        else:
            return Response({"success": False, "msg": 'Invalid Notification id'}, status=status.HTTP_400_BAD_REQUEST)
