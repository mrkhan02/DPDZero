# Generated by Django 4.2.4 on 2023-08-07 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_remove_customuser_age_remove_customuser_full_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="full_name",
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name="customuser",
            name="gender",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
