from django.db import models
from django.conf import settings


class Skill(models.Model):
    name = models.CharField(max_length=200)

    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="Users",
    )

    def __str__(self):
        return self.name


class HelpRequest(models.Model):
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="requester",
    )

    helper = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="helper",
        null=True,
        blank=True,
    )

    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)
