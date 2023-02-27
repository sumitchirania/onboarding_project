from rest_framework import serializers
from ..models.subscriber import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['id', 'endpoint', 'public_key', 'auth_key', 'email', 'name', 'is_active']

