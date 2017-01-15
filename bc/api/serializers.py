from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from bc.api.models import BucketList


class BucketListSerializer(ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(max_length=255, required=False)
    date_created = serializers.DateTimeField(read_only=True,
                                             default=timezone.now())
    created_by = serializers.CharField(source='user_id', required=False)

    class Meta:
        model = BucketList
        fields = ('id', 'name', 'description', 'date_created', 'date_modified',
                  'created_by')
