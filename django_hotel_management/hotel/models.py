from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length = 100)
    occupancy_type = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    from_date = models.DateField()
    to_date = models.DateField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
