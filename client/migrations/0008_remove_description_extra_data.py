# Generated by Django 3.0.5 on 2020-04-17 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_auto_20200417_0535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='extra_data',
        ),
    ]
