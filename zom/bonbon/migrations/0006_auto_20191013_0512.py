# Generated by Django 2.2.4 on 2019-10-12 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonbon', '0005_auto_20191013_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bill',
            name='day',
            field=models.CharField(max_length=20),
        ),
    ]
