# Generated by Django 3.0.5 on 2020-07-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_motivation_small_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_us_big',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='-')),
                ('content', models.TextField(default='-')),
                ('picture', models.FileField(blank=True, null=True, upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='About_us_small',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='-')),
                ('content', models.TextField(default='-')),
            ],
        ),
        migrations.CreateModel(
            name='Team_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Position', models.CharField(max_length=200)),
                ('email', models.TextField(default='-')),
                ('website', models.TextField(default='-')),
            ],
        ),
    ]
