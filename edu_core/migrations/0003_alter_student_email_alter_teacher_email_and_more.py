# Generated by Django 4.2.16 on 2024-12-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edu_core", "0002_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]