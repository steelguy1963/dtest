from django.contrib import admin
from .models import Invest, Column, AutoCat
# from .models import Comment

# Register your models here.

admin.site.register(Invest)
admin.site.register(Column)
admin.site.register(AutoCat)