# Generated by Django 5.0.4 on 2024-05-02 21:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stats", "0009_followclick"),
    ]

    operations = [
        migrations.AddField(
            model_name="daily",
            name="css_accounts",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="daily",
            name="css_posts",
            field=models.IntegerField(default=0),
        ),
    ]
