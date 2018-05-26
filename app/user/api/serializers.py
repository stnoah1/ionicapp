from rest_framework import serializers

from rest_framework.authtoken.models import Token

from user.models import YouAreUser, Friends


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = (
            'key'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouAreUser
        fields = (
            'phone', 'first_name', 'gender', 'birthday',
            'current_join_step'
        )


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = (
            'phone', 'name'
        )
