# Generated by Django 3.0.5 on 2020-04-17 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counsellor', '0005_counsellordata_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counsellordata',
            name='Profile_pic',
        ),
    ]
