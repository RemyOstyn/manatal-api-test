# Generated by Django 4.0.2 on 2022-02-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manatal', '0002_remove_student_id_alter_student_identification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='identification',
            field=models.CharField(default='5cRd5QW52T9dWGxdYZgw', editable=False, max_length=20, primary_key=True, serialize=False),
        ),
    ]
