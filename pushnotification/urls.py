from django.urls import path
from .views.push_notification import PushNotificationView

urlpatterns = [
    path("push-notification/", PushNotificationView.as_view(), name="push_notification"),
]