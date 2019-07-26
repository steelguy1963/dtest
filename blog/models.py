from django.db import models
from django.urls import reverse

# Create your models here.

class Column(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.IntegerField(null=True,blank=False)
    data = models.CharField(max_length=100,null=True,blank=False)
    title = models.CharField(max_length=100,null=True,blank=False)
    typed = models.CharField(max_length=100,null=True,blank=True)
    source = models.CharField(max_length=100,null=True,blank=True)
    renderer = models.CharField(max_length=100,null=True,blank=True)

class Post(models.Model):
    row_id = models.IntegerField(null=False,blank=False)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    value = models.CharField(max_length=100,null=True,blank=False)