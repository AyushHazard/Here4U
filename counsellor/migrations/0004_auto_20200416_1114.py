# Generated by Django 3.0.5 on 2020-04-16 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counsellor', '0003_auto_20200416_1112'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Userdata',
            new_name='Counsellordata',
        ),
    ]