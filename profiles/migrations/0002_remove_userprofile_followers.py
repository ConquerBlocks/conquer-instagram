# Generated by Django 5.1.2 on 2024-11-04 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="followers",
        ),
    ]
