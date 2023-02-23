from rest_framework import serializers
from ..models.subscriber import Subscriber


class SubscriberSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    endpoint = serializers.CharField(max_length=1024)
    public_key = serializers.CharField(max_length=1024)
    auth_key = serializers.CharField(max_length=1024)
    name = serializers.CharField(required=False, allow_blank=True, max_length=64)
    email = serializers.CharField(required=False, allow_blank=True, max_length=64)
    is_active = serializers.BooleanField(required=False, default=True)

    def create(self, validated_data):

        return Subscriber.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.endpoint = validated_data.get('endpoint', instance.endpoint)
        instance.public_key = validated_data.get('public_key', instance.public_key)
        instance.auth_key = validated_data.get('auth_key', instance.auth_key)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['id', 'endpoint', 'public_key', 'auth_key', 'email', 'name', 'is_active']

