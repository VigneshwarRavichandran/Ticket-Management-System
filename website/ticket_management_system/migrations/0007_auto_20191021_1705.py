# Generated by Django 2.2.6 on 2019-10-21 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_management_system', '0006_auto_20191021_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_by',
            new_name='createdby',
        ),
    ]