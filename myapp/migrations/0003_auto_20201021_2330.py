# Generated by Django 3.1.2 on 2020-10-21 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201019_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creared_by',
            new_name='created_by',
        ),
    ]
