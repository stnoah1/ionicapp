from django.db.models import Q
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from praise.api.serializers import PraiseSerializer, PraiseHistorySerializer
from praise.models import Praise, PraiseHistory


class PraiseListView(generics.ListAPIView):
    queryset = Praise.objects.all()
    serializer_class = PraiseSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    pagination_class.default_limit = 100

    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('code',)

    def list(self, request, *args, **kwargs):
        shuffle = self.request.GET.get('shuffle', None)
        queryset = self.filter_queryset(self.get_queryset())

        # shuffle
        if shuffle == 'true':
            req_count = int(self.request.GET.get('count', 1))
            queryset = queryset.order_by('?')[:req_count]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PraiseHistoryListView(generics.ListCreateAPIView):
    queryset = PraiseHistory.objects.all()
    serializer_class = PraiseHistorySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    pagination_class.default_limit = 100

    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('code',)

    def list(self, request, *args, **kwargs):
        user_key = request.user.phone

        queryset = self.filter_queryset(self.get_queryset())

        q = Q(receiver_key=user_key) | Q(sender_key=user_key)
        queryset = queryset.filter(q)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
