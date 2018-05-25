from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from user.api.serializers import UserSerializer
from user.models import Device, YouAreUser


@api_view(['POST'])
@permission_classes((IsAdminUser,))
def user_create_view(request):
    device_unique_key = request.data.get('device_unique_key')
    phone = request.data.get('phone')

    users = YouAreUser.objects.filter(phone=phone)
    if users.exists():
        user = users.first()
    else:
        user = YouAreUser.objects.create(phone=phone)

    Device.objects.create(user=user, unique_key=device_unique_key)

    token = Token.objects.filter(user=user).first().key
    return Response({'token': token}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def user_detail_view(request, token):
    user = Token.objects.filter(key=token).first().user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
