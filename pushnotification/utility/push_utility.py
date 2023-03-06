import json

from pywebpush import webpush
from pywebpush import WebPushException
from django.conf import settings


class PushNotificationUtility:

    PRIVATE_KEY = settings.PRIVATE_KEY
    ADMIN_MAIL = settings.ADMIN_EMAIL

    def send(self, subscription_data, notification_data):
        try:
            response = webpush(
                subscription_info=subscription_data,
                data=json.dumps(notification_data),
                vapid_private_key=PushNotificationUtility.PRIVATE_KEY,
                vapid_claims={
                    'sub': 'mailto:{}'.format(PushNotificationUtility.ADMIN_MAIL),
                }
            )
            if response.ok:
                return response
            raise WebPushException("Web push error {}".format(response.text))
        except WebPushException as e:
            raise WebPushException("Web push error {}".format(e))
