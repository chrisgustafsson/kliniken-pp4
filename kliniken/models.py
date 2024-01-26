from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
