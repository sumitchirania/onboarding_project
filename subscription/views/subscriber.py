import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..services.subscriber_service import SubscriberService
from ..serializers.subscribers_serializer import SubscriberSerializer

logger = logging.getLogger(__name__)


class SubscriberView(APIView):

    def get(self, request):

        subscriber_list = SubscriberService().get_subscribers()
        data = SubscriberSerializer(subscriber_list, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = SubscriberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subscriber = SubscriberService().create_subscriber(serializer.validated_data)
        return Response(SubscriberSerializer(subscriber).data, status=status.HTTP_201_CREATED)

