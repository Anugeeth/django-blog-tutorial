from django.db import models

# importing timezone or date_posted and Users from auth model for author
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

#  to see the sql code corresponding to the model,
#  $ python manage.py sqlmigrate <app_name> <migration_no> 
#  example  $ python manage.py sqlmigrate blog 0001