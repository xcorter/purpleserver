from rest_framework import serializers
from api.models import Mark

class MarkSerializer(serializers.Serializer):
    key = serializers.CharField(read_only=True, source='id')
    message = serializers.CharField(required=True, allow_blank=False)
    coordinate = serializers.CharField(required=True)

    def create(self, validated_data):
        message = validated_data.get('message', None)
        coordinate = validated_data.get('coordinate', None)
        return Mark.objects.create(message=message, coordinate=coordinate)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Mark` instance, given the validated data.
        """
        instance.message = validated_data.get('message', instance.message)
        instance.coordinate = validated_data.get('coordinate', instance.coordinate)
        instance.save()
        return instance
