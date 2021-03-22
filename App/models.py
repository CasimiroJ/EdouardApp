from django.db import models


class Team(models.Model):
    TeamId = models.IntegerField()
    Name = models.CharField(max_length=200)
    Size = models.IntegerField()
    Goal = models.IntegerField()
    Realized = models.IntegerField()
