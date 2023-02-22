
from django.db import models

from .mixins import DateTimeFieldMixin


class Subscriber(DateTimeFieldMixin):
    endpoint = models.CharField('subscriber_end_point', max_length=1024)
    public_key = models.CharField("subscriber_public_key", max_length=1024)
    auth_key = models.CharField("subscriber_auth_key", max_length=1024)
    name = models.CharField(max_length=64, blank=True, default="")
    email = models.CharField(max_length=64, blank=True, default="")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "subscriber"
        verbose_name = "subscriber"
        verbose_name_plural = "subscribers"
