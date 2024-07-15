from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    year_start = models.IntegerField(blank=True ,max_length=4)
    year_end = models.IntegerField(null=True, blank=True)
    skills_used = models.CharField(max_length=200, blank=True)
    
    
    def __str__(self):
        return self.title
