# Generated by Django 2.1.8 on 2019-07-29 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0008_auto_20190729_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='col_show',
            field=models.IntegerField(blank=True),
        ),
    ]
