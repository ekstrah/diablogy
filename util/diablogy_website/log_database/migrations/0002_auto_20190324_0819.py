# Generated by Django 2.1.7 on 2019-03-24 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_database', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Error',
        ),
        migrations.DeleteModel(
            name='Fullstack',
        ),
        migrations.DeleteModel(
            name='Openstack',
        ),
        migrations.DeleteModel(
            name='Pytest',
        ),
        migrations.DeleteModel(
            name='Teststack',
        ),
    ]