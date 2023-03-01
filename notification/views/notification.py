import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..services.notification_services import NotificationService
from ..serializers.notifications_serializer import NotificationSerializer

logger = logging.getLogger(__name__)


class NotificationView(APIView):

    def get(self, request):

        notification_list = NotificationService().get_notifications()
        data = NotificationSerializer(notification_list, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification = NotificationService().create_notification(serializer.validated_data)
        return Response(NotificationSerializer(notification).data, status=status.HTTP_201_CREATED)

