from rest_framework import serializers

from .models import Tag, New


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class NewSerializer(serializers.ModelSerializer):
    # view = serializers.IntegerField(source='hit_count.hits', read_only=True)

    class Meta:
        model = New
        fields = ['id', 'title', 'image', 'content', 'view', 'tag', 'created_at']
