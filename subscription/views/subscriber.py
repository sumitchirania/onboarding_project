import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..services.subscriber_service import SubscriberService
from ..serializers.subscribers_serializer import SubscriberSerializer

logger = logging.getLogger(__name__)


class SubscriberView(APIView):

    def get(self, request):

        subscriber_list = SubscriberService().get_subscribers_list()
        return Response(SubscriberSerializer(subscriber_list, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            subscriber = SubscriberService().create_subscriber(serializer.validated_data)
            return Response(SubscriberSerializer(subscriber).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

