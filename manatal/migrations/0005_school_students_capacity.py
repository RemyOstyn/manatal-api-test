# Generated by Django 4.0.2 on 2022-02-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manatal', '0004_alter_student_identification'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='students_capacity',
            field=models.PositiveSmallIntegerField(default=5),
        ),
    ]
