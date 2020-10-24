from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Avg
import numpy as np

# Create your models here.
class Profile(models.Model):