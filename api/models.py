import string
import random
from datetime import date, timedelta
from django.db import models
from django.contrib.auth.models import User


def generate_short_link():
    length = 5
    characters = string.ascii_letters + string.digits
    short_link = ""
    i = 0
    while (i < length):
        short_link += random.choice(characters)
        i += 1
    while Shorterlink.objects.filter(short_link=short_link).exists():
        short_link = generate_short_link()
    return short_link


def generate_expiration():
    today = date.today()
    expiration = today + timedelta(days=365)
    return expiration


class Shorterlink (models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    clicks = models.IntegerField(default=0)
    last_click = models.DateField(blank=True, null=True, default=None)
    link = models.CharField(max_length=50, unique=True)
    short_link = models.CharField(
        max_length=50, blank=True, null=True, unique=True)
    expiration = models.DateField(blank=True, null=True,)

    def save(self, *args, **kwargs):
        if not self.short_link:
            self.short_link = generate_short_link()
            self.expiration = generate_expiration()
        super().save(*args, **kwargs)
