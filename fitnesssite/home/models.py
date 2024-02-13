from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from stream_fields import blocks
from wagtail.snippets.blocks import SnippetChooserBlock


class HomePage(Page):
    body = RichTextField(blank=True)

    content = StreamField(
        [
            ("title", blocks.TitleBlock()),
            ("cards", blocks.CardsListBlock()),
            ("image_and_text", blocks.ImageAndTextBlock()),
            ("call_to_action", blocks.CallToActionBlock()),
            ("frequently_asked_questions", blocks.FAQBlock()),
            ("multi_step", blocks.MultiStepProcessBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("content"),
    ]
