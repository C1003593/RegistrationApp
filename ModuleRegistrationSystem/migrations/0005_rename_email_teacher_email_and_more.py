# Generated by Django 4.2.6 on 2023-12-18 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleRegistrationSystem', '0004_alter_registration_dateofregistration_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Module',
            new_name='module',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Picture',
            new_name='picture',
        ),
    ]
