# Generated by Django 2.1.8 on 2019-07-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0003_remove_column_col_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='col_data',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='column',
            name='col_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='cat',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_A',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_B',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_C',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_D',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_E',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_F',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_G',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_H',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_I',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_J',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_K',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_L',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_M',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_N',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='col_O',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='lev3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='lev4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='invest',
            name='team',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
