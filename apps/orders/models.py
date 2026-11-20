from django.conf import settings
from django.db import models

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "در انتظار تأیید"),
        ("confirmed","تأیید شده"),
        ("preparing", "در حال آماده‌سازی"),
        ("ready", "آماده تحویل"),
        ("completed", "تکمیل شده"),
        ("cancelled", "لغو شده"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="orders",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )

    food = models.ForeignKey(
        "menu.Food",
        on_delete=models.PROTECT,
    )

    food_name = models.CharField(
        max_length=150,
    )

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    quantity = models.PositiveBigIntegerField()

    line_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )