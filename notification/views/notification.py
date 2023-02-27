import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..services.notification_services import NotificationServices
from ..serializers.notifications_serializer import NotificationSerializer

logger = logging.getLogger(__name__)


class NotificationView(APIView):

    def get(self, request):

        notification_list = NotificationServices().get_notifications_list()
        return Response(NotificationSerializer(notification_list, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            notification = NotificationServices().create_notification(serializer.validated_data)
            return Response(NotificationSerializer(notification).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

