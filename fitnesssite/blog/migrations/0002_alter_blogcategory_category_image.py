# Generated by Django 5.0.1 on 2024-02-20 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogcategory",
            name="category_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Category Image to display as a thumbnail (resized to 150x150).",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="wagtailimages.image",
                verbose_name="Category Image",
            ),
        ),
    ]
