# Generated by Django 4.2.6 on 2023-12-18 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleRegistrationSystem', '0005_rename_email_teacher_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='module',
            new_name='Module',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='picture',
            new_name='Picture',
        ),
    ]