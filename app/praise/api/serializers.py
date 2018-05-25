from rest_framework import serializers

from praise.models import Praise


class PraiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Praise
        fields = (
            'content',
        )
