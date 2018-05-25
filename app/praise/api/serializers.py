from rest_framework import serializers

from praise.models import Praise, PraiseHistory


class PraiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Praise
        fields = (
            'content',
        )


class PraiseHistorySerializer(serializers.ModelSerializer):
    praise_content = PraiseSerializer(read_only=True, source='praise')

    class Meta:
        model = PraiseHistory
        fields = (
            'praise', 'praise_content',
            'choices', 'sender_key', 'receiver_key'
        )
