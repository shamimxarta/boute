from django.conf import settings
from django.db import models

# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=50)

    capacity = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "در انتظار تأیید"),
        ("confirmed", "تأیید شده"),
        ("cancelled", "لغو شده"),
        ("completed", "انجام شده"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="reservations",
    )

    table = models.ForeignKey(
        Table,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    reservation_date = models.DateField()

    reservation_time = models.TimeField()

    guest_count = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)