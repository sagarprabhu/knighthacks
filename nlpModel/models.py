from django.db import models

# Create your models here.
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class nlpModel(models.Model):

    question = models.CharField(max_length=400)
