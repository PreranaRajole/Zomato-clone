# Generated by Django 2.2.4 on 2019-10-12 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bonbon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('bill', models.CharField(max_length=100, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='res',
            fields=[
                ('res_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=30)),
                ('cuisine', models.CharField(max_length=300)),
                ('timings', models.CharField(max_length=300, null=True)),
                ('avg_rating', models.CharField(max_length=5)),
                ('avg_price', models.CharField(max_length=10)),
                ('link', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='searchval',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=20, null=True)),
                ('search', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='visits',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(max_length=300, null=True)),
                ('checked', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='search',
        ),
    ]
