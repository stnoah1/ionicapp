from django.contrib.postgres.fields import JSONField
from django.db import models

from service.models import TimeStampedModel


class Praise(TimeStampedModel):
    class Meta:
        verbose_name = '칭찬'
        verbose_name_plural = verbose_name

    content = models.CharField(verbose_name='내용', unique=True, max_length=200)


class PraiseHistory(TimeStampedModel):
    class Meta:
        verbose_name = '칭찬 내역'
        verbose_name_plural = verbose_name

    praise = models.ForeignKey(Praise, verbose_name='칭찬')
    choices = JSONField(verbose_name='칭찬 대상 목록')

    sender_key = models.CharField(verbose_name='보낸 사람 user key', max_length=200)
    receiver_key = models.CharField(verbose_name='받은 사람 user key', max_length=200)
