from django.db import models
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alertName = models.CharField(max_length=50)
    amount = models.IntegerField()
    operator = models.CharField(max_length=50)
    currency = models.IntegerField()
