# Generated by Django 2.2.6 on 2019-10-21 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_management_system', '0005_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='created_by',
        ),
    ]