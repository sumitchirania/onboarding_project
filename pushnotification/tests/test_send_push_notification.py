# Print and mocking + celery tests
import json

from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

from notification.services.notification_services import NotificationService


class TestPushNotification(TestCase):
    def setUp(self):

        self.client = Client()
        self.notification = {
            "title": "Sale! Sale! Sale!",
            "desc": "BOGO Offer is live."
        }
        self.valid_notification_id = {"notification_id": 1}
        self.invalid_notification_id = {"notification_id": ""}
        self.notification_not_exists_id = {"notification_id": 100000}

    @patch("pushnotification.tasks.task_push_notification.task_send_notification")
    def test_valid_push_notification(self, mock_task):

        notification = NotificationService().create_notification(self.notification)
        self.valid_notification_id["notification_id"] = notification.id

        response = self.client.post(
            reverse('push_notification'),
            data=json.dumps(self.valid_notification_id),
            content_type='application/json'
        )
        # mock_task.assert_called_once()
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_invalid_push_notification(self):
        response = self.client.post(
            reverse('push_notification'),
            data=json.dumps(self.invalid_notification_id),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_notification_not_exists_push_notification(self):

        response = self.client.post(
            reverse('push_notification'),
            data=json.dumps(self.notification_not_exists_id),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
