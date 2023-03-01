from django.urls import path
from .views.notification import NotificationView

urlpatterns = [
    path("notifications/", NotificationView.as_view(), name="notifications"),
]