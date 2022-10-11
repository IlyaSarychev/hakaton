from django.db import models

from account.models import User


class ProjectApplication(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apps", unique=False)

    title = models.CharField("Название проекта", max_length=255)
    goal = models.TextField("Цель")
    result = models.TextField("Результат")
    criteria = models.TextField("Критерии приемки")
    description = models.TextField("Описание проекта")
    max_instances = models.PositiveSmallIntegerField("Макс количество экземпляров проекта", default=1)

    objects = models.Manager()
