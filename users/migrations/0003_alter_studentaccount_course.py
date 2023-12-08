# Generated by Django 4.2.6 on 2023-12-08 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleRegistrationSystem', '0001_initial'),
        ('users', '0002_studentaccount_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentaccount',
            name='Course',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModuleRegistrationSystem.course'),
        ),
    ]
