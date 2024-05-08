# Generated by Django 5.0.1 on 2024-02-27 16:41

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_blogcategory_short_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogdetailpage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "title",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        help_text="Text of the title", required=True
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "cards",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "cards",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Title text for the card (100 charecters max.)",
                                                        max_length=100,
                                                    ),
                                                ),
                                                (
                                                    "text",
                                                    wagtail.blocks.TextBlock(
                                                        help_text="Optional card text. (255 characters max.)",
                                                        max_length=255,
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        help_text="Image will be automatically cropped for performance"
                                                    ),
                                                ),
                                                (
                                                    "link",
                                                    wagtail.blocks.StructBlock(
                                                        [
                                                            (
                                                                "link_text",
                                                                wagtail.blocks.CharBlock(
                                                                    default="Read More",
                                                                    max_length=50,
                                                                ),
                                                            ),
                                                            (
                                                                "internal_page",
                                                                wagtail.blocks.PageChooserBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                            (
                                                                "external_link",
                                                                wagtail.blocks.URLBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                        ],
                                                        help_text="Select a page or input a valid External URL.",
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "image_and_text",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        help_text="Image will be automatically cropped for performance"
                                    ),
                                ),
                                (
                                    "image_alignment",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[("left", "Left"), ("right", "Right")],
                                        help_text="Choose alignment of the image",
                                    ),
                                ),
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="60 characters max", max_length=60
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.TextBlock(
                                        max_length=140, required=False
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "link_text",
                                                wagtail.blocks.CharBlock(
                                                    default="Read More", max_length=50
                                                ),
                                            ),
                                            (
                                                "internal_page",
                                                wagtail.blocks.PageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "external_link",
                                                wagtail.blocks.URLBlock(required=False),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "call_to_action",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="100 characters max.", max_length=100
                                    ),
                                ),
                                (
                                    "subtitle",
                                    wagtail.blocks.CharBlock(
                                        blank=True,
                                        help_text="200 characters max.",
                                        max_length=200,
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "link_text",
                                                wagtail.blocks.CharBlock(
                                                    default="Read More", max_length=50
                                                ),
                                            ),
                                            (
                                                "internal_page",
                                                wagtail.blocks.PageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "external_link",
                                                wagtail.blocks.URLBlock(required=False),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "background_image",
                                    wagtail.images.blocks.ImageChooserBlock(),
                                ),
                            ]
                        ),
                    ),
                    (
                        "frequently_asked_questions",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="100 characters max.", max_length=100
                                    ),
                                ),
                                (
                                    "questions",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "asked_question",
                                                    wagtail.blocks.TextBlock(
                                                        help_text="FAQ Question",
                                                        max_length=200,
                                                    ),
                                                ),
                                                (
                                                    "answer",
                                                    wagtail.blocks.RichTextBlock(
                                                        help_text="FAQ Answer",
                                                        max_length=200,
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "multi_step",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Section title 100 characters max.",
                                        max_length=100,
                                    ),
                                ),
                                (
                                    "steps",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "step_title",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Individual step title, 100 characters max.",
                                                        max_length=100,
                                                    ),
                                                ),
                                                (
                                                    "step_description",
                                                    wagtail.blocks.TextBlock(
                                                        help_text="A short desctiption of the step",
                                                        max_length=200,
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("rich_text", wagtail.blocks.RichTextBlock()),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
