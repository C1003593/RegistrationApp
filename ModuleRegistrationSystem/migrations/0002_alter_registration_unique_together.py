# Generated by Django 4.2.6 on 2023-12-11 20:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ModuleRegistrationSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together={('student', 'module')},
        ),
    ]