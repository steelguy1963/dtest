# Generated by Django 2.1.8 on 2019-07-29 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0009_auto_20190729_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invest',
            name='updated_at',
        ),
    ]