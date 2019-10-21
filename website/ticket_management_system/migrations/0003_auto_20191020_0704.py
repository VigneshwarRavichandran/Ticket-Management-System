# Generated by Django 2.2.6 on 2019-10-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_management_system', '0002_auto_20191020_0627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='usersystem',
            name='posts',
            field=models.ManyToManyField(blank=True, to='ticket_management_system.Post'),
        ),
    ]
