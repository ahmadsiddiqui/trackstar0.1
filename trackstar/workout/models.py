from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
	
	class ActivityType(models.TextChoices):
		CARDIO = 'C'
		WEIGHTS = 'W'

	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)
	ActivityType = models.CharField(
		max_length = 1, choices = ActivityType.choices, default = 'WEIGHTS')
	user = models.ForeignKey(User, on_delete = models.CASCADE, default = '0')
