# Generated by Django 2.2.7 on 2020-03-30 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_user_additional_data_user_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_additional_data',
        ),
        migrations.DeleteModel(
            name='user_details',
        ),
    ]
