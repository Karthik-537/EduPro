# Generated by Django 4.2.16 on 2024-12-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edu_core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]