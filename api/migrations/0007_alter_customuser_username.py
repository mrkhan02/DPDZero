# Generated by Django 4.2.4 on 2023-08-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_remove_customuser_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]