# Generated by Django 2.1.8 on 2019-07-29 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0007_auto_20190729_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='col_show',
            field=models.BooleanField(blank=True, default=True),
            preserve_default=False,
        ),
    ]
