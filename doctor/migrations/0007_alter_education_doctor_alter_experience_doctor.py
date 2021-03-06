# Generated by Django 4.0.2 on 2022-04-25 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_doctorprofile_specialties_delete_specialty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='doctor.doctorprofile'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='doctor.doctorprofile'),
        ),
    ]
