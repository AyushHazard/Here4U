# Generated by Django 3.0.5 on 2020-04-17 05:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('counsellor', '0004_auto_20200416_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='counsellordata',
            name='Profile_pic',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]