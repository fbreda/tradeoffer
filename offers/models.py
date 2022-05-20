from django.db import models
from users.models import User


class Offer(models.Model):
    offer_title = models.CharField(max_length=120)
    offer_description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Offer")
        verbose_name_plural = ("Offers")

    def __str__(self):
        return self.offer_title

    objects = models.Manager()
