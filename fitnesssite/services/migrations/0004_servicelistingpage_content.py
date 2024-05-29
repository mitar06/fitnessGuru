# Generated by Django 5.0.1 on 2024-05-09 13:22

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0003_alter_servicepage_service_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicelistingpage",
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
                    (
                        "newsletter_subscribe",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Main title for this section (max 200 characters)",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "subtitle",
                                    wagtail.blocks.CharBlock(
                                        help_text="Subtitle for this section (max 200 characters)",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "button_text",
                                    wagtail.blocks.CharBlock(
                                        default="Subscribe",
                                        help_text="Text for the submit button",
                                        max_length=20,
                                    ),
                                ),
                                (
                                    "disclaimer_text",
                                    wagtail.blocks.CharBlock(
                                        help_text="Text disclaiming Terms and Conditions",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "terms_and_conditions_link",
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
                        "timeline",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Main title for this section (max 200 characters)",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "subtitle",
                                    wagtail.blocks.CharBlock(
                                        help_text="Optional subtitle, (max 200 characters)",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "items",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "marker_caption",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Text for the left side marker of the timeline",
                                                        max_length=50,
                                                    ),
                                                ),
                                                (
                                                    "title_primary",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Bold title on the right site of the timeline",
                                                        max_length=50,
                                                    ),
                                                ),
                                                (
                                                    "title_secondary",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Cursive title above the primary title",
                                                        max_length=50,
                                                    ),
                                                ),
                                                (
                                                    "content",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Content describing the individual timeline item.",
                                                        max_length=50,
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
                        "why_us",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "pill_caption",
                                    wagtail.blocks.CharBlock(
                                        help_text="Main title for this section (max 50 characters).",
                                        max_length=50,
                                    ),
                                ),
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Main title for this section (max 200 characters).",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "subtitle",
                                    wagtail.blocks.CharBlock(
                                        help_text="Optional subtitle, (max 200 characters).",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "featured_cards",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "icon",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        help_text="Icon to be displayed in a card, will be downscaled for performance.",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Main title for this section (max 200 characters).",
                                                        max_length=200,
                                                    ),
                                                ),
                                                (
                                                    "content",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="A short description of the card.",
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
                        "free_products",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Main title for this section (max 200 characters).",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "subtitle",
                                    wagtail.blocks.CharBlock(
                                        help_text="Optional subtitle, (max 200 characters).",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "free_product_cards",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "card_image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        help_text="Background image for the card, will be overlayed by text."
                                                    ),
                                                ),
                                                (
                                                    "product_link",
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
                                                        ]
                                                    ),
                                                ),
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Main title for this section (max 200 characters).",
                                                        max_length=200,
                                                    ),
                                                ),
                                                (
                                                    "content",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Main content for the card (max 200 characters).",
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
                        "plan_showcase",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Main title for this section (max 200 characters).",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "subtitle",
                                    wagtail.blocks.CharBlock(
                                        help_text="Optional subtitle, (max 200 characters).",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "list_items",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "text",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="A single feature of the product.",
                                                        max_length=200,
                                                    ),
                                                )
                                            ]
                                        ),
                                        max_num=6,
                                    ),
                                ),
                                (
                                    "showcase_image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        help_text="Image to be displayed with the plan breakdown."
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "services_header",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Main title for this section (max 200 characters).",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "images",
                                    wagtail.blocks.ListBlock(
                                        wagtail.images.blocks.ImageChooserBlock(),
                                        max_num=2,
                                    ),
                                ),
                                (
                                    "text_content",
                                    wagtail.blocks.TextBlock(
                                        help_text="Main text content, 500 chanacters max.",
                                        max_length=500,
                                        required=True,
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
