# Generated by Django 3.1.4 on 2020-12-31 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0002_auto_20201227_0326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='djangoclasses',
            old_name='instructorName',
            new_name='instructor_Name',
        ),
        migrations.RemoveField(
            model_name='djangoclasses',
            name='courseNumber',
        ),
        migrations.AddField(
            model_name='djangoclasses',
            name='course_Number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]