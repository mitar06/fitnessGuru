from django.core.exceptions import ValidationError
from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import StreamField
from wagtail import blocks as base_blocks
from stream_fields import blocks

# Create your models here.
from wagtail.models import Page


class ServiceListingPage(Page):
    subtitle = models.TextField(
        blank=True,
        max_length=1000,
    )

    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        help_text="Select a banner Image for Services Listing page",
        related_name="+",
        on_delete=models.SET_NULL,
    )

    banner_title = models.TextField(
        blank=True,
        max_length=500,
    )

    content = StreamField(
        [
            ("title", blocks.TitleBlock()),
            ("cards", blocks.CardsListBlock()),
            ("image_and_text", blocks.ImageAndTextBlock()),
            ("call_to_action", blocks.CallToActionBlock()),
            ("frequently_asked_questions", blocks.FAQBlock()),
            ("multi_step", blocks.MultiStepProcessBlock()),
            ("newsletter_subscribe", blocks.NewsletterEmailCollectionBlock()),
            ("timeline", blocks.TimelineBlock()),
            ("why_us", blocks.WhyUsBlock()),
            ("free_products", blocks.FeaturedFreeProductBlock()),
            ("plan_showcase", blocks.SinglePlanBreakdownAndImageBlock()),
            ("services_header", blocks.ServicesListingPageHeaderBlock()),
            ('rich_text', base_blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("banner_image"),
        FieldPanel("banner_title"),
        FieldPanel("content")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(ServiceListingPage, self).get_context(request, *args, **kwargs)
        context["services"] = ServicePage.objects.live().public()
        return context


class ServicePage(Page):
    description = models.TextField(
        blank=True,
        max_length=1000,
    )
    internal_page = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        help_text="Select and Internal Wagtail Page",
        on_delete=models.SET_NULL,
    )
    external_page = models.URLField(blank=True)
    button_text = models.CharField(blank=True, max_length=50)
    service_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="This image is used on a services listing page and it will \
             be cropped for optimization ",
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        PageChooserPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("service_image"),
        FieldPanel("button_text"),
    ]

    def clean(self):
        super(ServicePage, self).clean()

        if self.internal_page and self.external_page:
            raise ValidationError(
                {
                    "internal_page": ValidationError(
                        "Please Choose internal page or external page, not both."
                    ),  # noqa: E501
                    "external_page": ValidationError(
                        "Please Choose internal page or external page, not both."
                    ),  # noqa: E501
                }
            )
