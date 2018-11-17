from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
from django.db.models import CASCADE


class Token(models.Model):
    token = models.CharField(max_length=10, null=False, blank=False, unique=True)
    amount = models.IntegerField(null=False, default=10)
    used = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({}, {})".format(self.token, self.amount, self.used)


class ExchangeUser(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    credit = models.IntegerField(null=False, default=10)

    def __str__(self):
        return "{} ({})".format(self.user.username, self.credit)
