# Generated by Django 3.0.5 on 2020-05-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_auto_20200524_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdata',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=32),
        ),
    ]
