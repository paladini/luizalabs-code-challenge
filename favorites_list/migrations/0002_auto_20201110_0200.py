# Generated by Django 3.1.3 on 2020-11-10 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favoritelist',
            unique_together=set(),
        ),
    ]
