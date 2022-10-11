from rest_framework import serializers

from account.serializers import UserSerializer
from .models import ProjectApplication


class ProjectApplicationSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = ProjectApplication
        fields = ["owner", "title", "goal", "result", "criteria", "description", "max_instances"]

    def save(self, **kwargs):
        return super().save(**kwargs, owner=self.context["request"].user)

