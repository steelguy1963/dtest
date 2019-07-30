from django.db import models

# Create your models here.

class Invest(models.Model):
    team = models.CharField(max_length=100,blank=True)
    cat = models.CharField(max_length=100,blank=True)
    lev3 = models.CharField(max_length=100,blank=True)
    lev4 = models.CharField(max_length=100,blank=True)
    col_A = models.CharField(max_length=100,blank=True)
    col_B = models.CharField(max_length=100,blank=True)
    col_C = models.CharField(max_length=100,blank=True)
    col_D = models.CharField(max_length=100,blank=True)
    col_E = models.CharField(max_length=100,blank=True)
    col_F = models.CharField(max_length=100,blank=True)
    col_G = models.CharField(max_length=100,blank=True)
    col_H = models.CharField(max_length=100,blank=True)
    col_I = models.CharField(max_length=100,blank=True)
    col_J = models.CharField(max_length=100,blank=True)
    col_K = models.CharField(max_length=100,blank=True)
    col_L = models.CharField(max_length=100,blank=True)
    col_M = models.CharField(max_length=100,blank=True)
    col_N = models.CharField(max_length=100,blank=True)
    col_O = models.CharField(max_length=100,blank=True)

class Column(models.Model):
    col_data = models.CharField(max_length=100,blank=True)
    col_title = models.CharField(max_length=100,blank=True)
    col_show = models.IntegerField(blank=True)
    
class Email(models.Model):
    to = models.EmailField(null=False, blank=False)
    subject_text = models.CharField(max_length=500,blank=False)
    body_text = models.TextField(blank=True)

class AutoCat(models.Model):
    auto_cat = models.CharField(max_length=100,blank=True)
    