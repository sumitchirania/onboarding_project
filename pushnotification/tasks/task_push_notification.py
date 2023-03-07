import logging

from celery import shared_task
from celery.exceptions import TaskError
from ..utility.push_utility import PushNotificationUtility

logger = logging.getLogger(__name__)


@shared_task()
def task_send_notification(subscriber, notification_data):

    logger.info("Creating push notification request for subscriber={} with notification_data {}".format(
        subscriber, notification_data)
    )
    PushNotificationUtility().send(
        subscription_data=subscriber,
        notification_data=notification_data
    )


@shared_task()
def task_calculate_sum(a, b):
    try:
        return a + b
    except TaskError:
        return None
