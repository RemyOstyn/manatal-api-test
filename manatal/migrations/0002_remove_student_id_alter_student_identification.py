# Generated by Django 4.0.2 on 2022-02-28 17:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manatal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='identification',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]