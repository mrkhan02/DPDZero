# Generated by Django 4.2.4 on 2023-08-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="key",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
