# Generated by Django 2.1.8 on 2019-07-30 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0011_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_cat', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
