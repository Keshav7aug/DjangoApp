from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    convID = models.TextField()
    IssueID = models.CharField(max_length=20)