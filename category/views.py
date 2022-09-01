from optparse import SUPPRESS_USAGE
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Category
from . import serializers


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer
    permission_classes = (permissions.IsAdminUser,)

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return serializers.CategoryListSerializer
    #     return serializers.CategoryDetailSerilizer

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #     else:
    #         permission_classes = (permissions.IsAdminUser,)
    #     return [permission() for permission in permission_classes]



