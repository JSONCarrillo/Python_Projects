# Generated by Django 3.1.4 on 2020-12-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('courseNumber', models.PositiveIntegerField(max_length=2)),
                ('instructorName', models.CharField(max_length=40)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
