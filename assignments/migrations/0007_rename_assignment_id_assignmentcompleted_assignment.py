# Generated by Django 3.2 on 2021-04-12 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0006_auto_20210412_0735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignmentcompleted',
            old_name='assignment_id',
            new_name='assignment',
        ),
    ]