# Generated by Django 5.0.1 on 2024-02-20 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_sitesettings"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesettings",
            name="fav_icon",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Icon to be displayed as fav-icon in page header (will be rezized).",
            ),
        ),
        migrations.AlterField(
            model_name="sitesettings",
            name="logo",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Business logo for navigation",
            ),
        ),
    ]
