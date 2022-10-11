from django.urls import path

from . import views


urlpatterns = [
    path("login/", views.LoginApiView.as_view(), name="login"),
    path("contractors/", views.ContractorListCreateAPIView.as_view(), name="contractors"),
    path("contractors/<int:pk>/", views.ContractorRetrieveUpdateDeleteAPIView.as_view(), name="retrieve_update_delete_contractor"),
    path("user/<int:pk>/", views.UserRetrieveUpdateDeleteAPIView.as_view(), name="retrieve_update_delete_user"),
    path("customers/", views.CustomerListCreateAPIView.as_view(), name="customers"),
    path("customer/<int:pk>/", views.CustomerRetrieveUpdateDeleteAPIView.as_view(), name="retrieve_update_delete_customer"),
]
