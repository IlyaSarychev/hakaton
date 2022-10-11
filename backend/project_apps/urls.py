from django.urls import path

from . import views


urlpatterns = [
    path("project_apps/", views.ProjectAppsListCreateAPIView.as_view(), name="project_apps"),
    path("project_app/<int:pk>/", views.ProjectAppsRetrieveUpdateDeleteAPIView.as_view(), name="project_app"),
]