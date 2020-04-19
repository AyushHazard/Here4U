# Generated by Django 3.0.5 on 2020-04-17 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellor', '0007_auto_20200417_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counsellordata',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='counsellordata',
            name='City',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='counsellordata',
            name='Education',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='counsellordata',
            name='Expertise',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='counsellordata',
            name='Profile_pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='counsellordata',
            name='State',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='counsellordata',
            name='Summary',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]