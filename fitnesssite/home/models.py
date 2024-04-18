from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from stream_fields import blocks
from wagtail.snippets.blocks import SnippetChooserBlock


from django.db import models
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.images.models import Image


@register_setting
class SiteSettings(BaseSiteSetting):
    logo = models.OneToOneField(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Business logo for navigation')
    fav_icon =  models.OneToOneField(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Icon to be displayed as fav-icon in page header (will be rezized).')
    panels = [
        FieldPanel('logo'),
        FieldPanel('fav_icon'),
    ]


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
            ('newsletter_subscribe', blocks.NewsletterEmailCollectionBlock()),
            ("timeline", blocks.TimelineBlock()),
            ('why_us',blocks.WhyUsBlock()),
            ("free_products", blocks.FeaturedFreeProductBlock()),
            ('plan_showcase', blocks.SinglePlanBreakdownAndImageBlock())
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("content"),
    ]
