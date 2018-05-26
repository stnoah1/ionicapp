from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from user.api.serializers import UserSerializer, FriendsSerializer
from user.models import Device, YouAreUser, Friends


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


@api_view(['GET', 'PATCH'])
@permission_classes((IsAuthenticated,))
def user_detail_view(request):
    user = request.user
    if request.method == 'PATCH':
        for k, v in request.data.items():
            setattr(user, k, v)
        user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


class FriendsListView(generics.ListAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    pagination_class.default_limit = 100

    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('code',)

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=user)

        shuffle = self.request.GET.get('shuffle', None)
        # shuffle
        if shuffle == 'true':
            req_count = int(self.request.GET.get('count', 4))
            queryset = queryset.order_by('?')[:req_count]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
