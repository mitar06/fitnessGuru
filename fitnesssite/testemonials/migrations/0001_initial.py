# Generated by Django 5.0.1 on 2024-02-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Testemonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField(max_length=500)),
                ("attribution", models.CharField(max_length=50)),
            ],
        ),
    ]
