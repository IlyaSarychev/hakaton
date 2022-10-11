from rest_framework import generics
from rest_framework.permissions import BasePermission

from account.views import method_permission_classes

from .models import ProjectApplication
from .serializers import ProjectApplicationSerializer


class IsCustomer(BasePermission):
    message = 'Только заказчик может создать заявку'

    def has_permission(self, request, view):
        return request.user.is_customer or request.user.is_superuser  # или суперпользователь


class ProjectAppsListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProjectApplication.objects.all()
    serializer_class = ProjectApplicationSerializer

    @method_permission_classes([IsCustomer])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProjectAppsRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectApplication.objects.all()
    serializer_class = ProjectApplicationSerializer

    @method_permission_classes([IsCustomer])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @method_permission_classes([IsCustomer])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @method_permission_classes([IsCustomer])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
