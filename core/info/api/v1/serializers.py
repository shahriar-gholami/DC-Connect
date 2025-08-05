from rest_framework import serializers
from ...models import Route

class LinkSerializer(serializers.Serializer):
    src_row = serializers.CharField(max_length=100)
    src_rack = serializers.CharField(max_length=100)
    src_pp = serializers.CharField(max_length=100)
    dst_row = serializers.CharField(max_length=100)
    dst_rack = serializers.CharField(max_length=100)
    dst_pp = serializers.CharField(max_length=100)

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'route']
        read_only_fields = ['id']






