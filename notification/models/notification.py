
from django.db import models

from .mixins import DateTimeFieldMixin


class Notification(DateTimeFieldMixin):
    title = models.CharField('Notification Title', max_length=255)
    desc = models.CharField("Notification Description", max_length=1024)

    class Meta:
        db_table = "notification"
        verbose_name = "notification"
        verbose_name_plural = "notifications"
