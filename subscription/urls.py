from django.urls import path
from .views.subscriber import SubscriberView

urlpatterns = [
    path("subscribers/", SubscriberView.as_view(), name="subscribers"),
]