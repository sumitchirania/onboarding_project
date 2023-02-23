import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..services.subscriber_crud import SubscriberCrud
from rest_framework.parsers import JSONParser
from ..serializers.subscribers_serializer import SubSerializer

logger = logging.getLogger(__name__)


class SubscriberView(APIView):

    def get(self, request):
        subscriber_list = SubscriberCrud().get_subscribers_list()
        return Response(SubSerializer(subscriber_list, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):

        data = JSONParser().parse(request)
        serializer = SubSerializer(data=data)
        print(serializer)
        print(vars(serializer))
        print(serializer.__dir__())
        if serializer.is_valid():
            subscriber = SubscriberCrud().create_subscriber(serializer.validated_data)
            return Response(SubSerializer(subscriber).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

