# Generated by Django 4.0.2 on 2022-04-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_rename_payment_doctorprofile_pricings'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='schedule',
            field=models.CharField(default='Monday, Friday, Saturday', max_length=200),
        ),
    ]
