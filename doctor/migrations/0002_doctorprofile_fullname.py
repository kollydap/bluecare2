# Generated by Django 4.0.2 on 2022-04-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='fullname',
            field=models.CharField(default='Dr Bezos Mike', max_length=200),
        ),
    ]