from django.contrib import admin
from .models import Post, Column
# from .models import Comment

# Register your models here.

@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'data', 'title', 'typed', 'source', 'renderer')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'row_id', 'column', 'value')  
