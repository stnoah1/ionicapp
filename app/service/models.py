from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField("생성일", auto_now_add=timezone.now)
    updated = models.DateTimeField("수정일", auto_now=timezone.now)

