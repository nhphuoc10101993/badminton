from rest_framework import serializers
from .models import BucketList
class BucketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketList
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
