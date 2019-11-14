# Generated by Django 2.1.7 on 2019-11-13 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_code', models.PositiveSmallIntegerField()),
                ('score', models.PositiveSmallIntegerField()),
                ('category', models.CharField(max_length=50)),
                ('prof', models.CharField(max_length=50)),
                ('time', models.TextField()),
                ('recommend_year', models.CharField(max_length=255)),
                ('weight', models.PositiveSmallIntegerField()),
                ('remarks', models.TextField()),
                ('link', models.URLField(max_length=255)),
                ('semester', models.CharField(max_length=255)),
            ],
        ),
    ]
