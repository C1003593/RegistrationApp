# Generated by Django 4.2.6 on 2023-12-05 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleRegistrationSystem', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentaccount',
            name='Course',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ModuleRegistrationSystem.course'),
        ),
    ]
