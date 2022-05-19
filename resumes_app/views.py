from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class ResumeReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class WishlistModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            wished_resume = Resume.objects.get(id=self.kwargs['pk'])
            return serializer.save(user=self.request.user, wished_resume=wished_resume)
        except:
            raise NotFound

    def get_queryset(self):
        if self.action == 'list' or self.action == 'retrieve':
            return Wishlist.objects.filter(user_id=self.request.user.id)
        elif self.action == 'post' or self.action == 'destroy':
            return Wishlist.objects.all()

    def get_serializer_class(self):
        try:
            if self.action == 'list':
                return WishlistSerializer
            if self.action == 'create':
                return WishlistCreateSerializer
            elif self.action == 'destroy':
                return WishlistDetailSerializer
            else:
                return WishlistSerializer
        except:
            raise AuthenticationFailed


class CategoriesViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializers(queryset, many=True)
        return Response(serializer.data)


class PartnerViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Partners.objects.all()
        serializer = PartnersSerializer(queryset, many=True)
        return Response(serializer.data)


