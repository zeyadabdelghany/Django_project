# Generated by Django 3.1.2 on 2020-10-19 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='board',
            table='Board',
        ),
        migrations.AlterModelTable(
            name='post',
            table='Post',
        ),
        migrations.AlterModelTable(
            name='topic',
            table='Topic',
        ),
    ]