from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework import views
from rest_framework import permissions
from rest_framework.response import Response

from .models import ContractorAccount, User, CustomerAccount
from .serializers import ContractorAccountSerializer, LoginSerializer, UserSerializer, CustomerAccountSerializer


def method_permission_classes(classes):
    def decorator(func):
        def decorated_func(self, *args, **kwargs):
            self.permission_classes = classes
            # this call is needed for request permissions
            self.check_permissions(self.request)
            return func(self, *args, **kwargs)
        return decorated_func
    return decorator


class LoginApiView(views.APIView):
    @method_permission_classes([permissions.AllowAny])
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            authenticate(email=serializer.data.get("email"), password=serializer.data.get("password"))
        return Response({"success": True})


class UserRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContractorListCreateAPIView(generics.ListCreateAPIView):
    queryset = ContractorAccount.objects.all()
    serializer_class = ContractorAccountSerializer
    permission_classes = [permissions.AllowAny]

    @method_permission_classes([permissions.IsAuthenticated])
    def get(self, request, *args, **kwargs):
        return super(ContractorListCreateAPIView, self).get(request, *args, **kwargs)


class ContractorRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContractorAccount.objects.all()
    serializer_class = ContractorAccountSerializer


class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomerAccount.objects.all()
    serializer_class = CustomerAccountSerializer
    permission_classes = [permissions.AllowAny]

    @method_permission_classes([permissions.IsAuthenticated])
    def get(self, request, *args, **kwargs):
        return super(CustomerListCreateAPIView, self).get(request, *args, **kwargs)


class CustomerRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerAccount.objects.all()
    serializer_class = CustomerAccountSerializer
