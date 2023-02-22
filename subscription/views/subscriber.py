import logging

from rest_framework.views import APIView
from ..services.subscriber_crud import SubscriberCrud
from django.http import JsonResponse

logger = logging.getLogger(__name__)


class SubscriberView(APIView):
    print(1111112233)

    def post(self, request):
        print(11111)
        print(request.data)
        endpoint = request.data['endpoint']
        auth_key = request.data['auth_key']
        public_key = request.data['public_key']
        print(endpoint, 'end', auth_key, 'auth', public_key)
        subscriber = SubscriberCrud()
        success = subscriber.create_subscriber(request.data)
        print(success, 'succ')
        if success:
            return JsonResponse({'success': True, 'status': 200, 'msg': 'Subscriber created'})
        else:
            return JsonResponse({'success': False, 'status': 500, 'msg': 'Subscriber could not be created'})


