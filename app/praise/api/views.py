from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from praise.api.serializers import PraiseSerializer
from praise.models import Praise


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
