from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import Device


@api_view(['POST'])
# @permission_classes((IsAdminUser,))
def token_retrieve_view(request):
    device_unique_key = request.data.get('device_unique_key')
    token = ''
    try:
        device = Device.objects.get(unique_key=device_unique_key)
        token = Token.objects.filter(user=device.user).first().key
    except Device.DoesNotExist:
        pass
    return Response({'token': token}, status=status.HTTP_201_CREATED if token else status.HTTP_204_NO_CONTENT)
