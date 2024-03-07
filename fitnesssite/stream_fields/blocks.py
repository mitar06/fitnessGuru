from django.db import models

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
# Create your models here.


class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, help_text="Text of the title")

    class Meta:
        template = "stream_fields/title_block.html"
        icon = "edit"
        label = "Title Block"
        help_text = "Centered heading text block."


class LinkValue(blocks.StructValue):
    def url(self) -> str:
        internal_page = self.get("internal_page")
        external_page = self.get("external_link")
        if internal_page:
            return internal_page.url
        elif external_page:
            return external_page
        return None


class GenericLink(blocks.StructBlock):
    link_text = blocks.CharBlock(max_length=50, default="Read More")
    internal_page = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)

    class Meta:
        value_class = LinkValue


class GenericCard(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100, help_text="Title text for the card (100 charecters max.)"
    )
    text = blocks.TextBlock(
        max_length=255,
        help_text="Optional card text. (255 characters max.)",
        required=False,
    )
    image = ImageChooserBlock(
        help_text="Image will be automatically cropped for performance"
    )
    link = GenericLink(help_text="Select a page or input a valid External URL.")


class CardsListBlock(blocks.StructBlock):
    cards = blocks.ListBlock(GenericCard())

    class Meta:
        template = "stream_fields/cards_block.html"
        icon = "image"
        label = "Generic Cards List"


class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        help_text="Image will be automatically cropped for performance"
    )
    image_alignment = blocks.ChoiceBlock(
        choices=(
            ("left", "Left"),
            ("right", "Right"),
        ),
        default="left",
        help_text="Choose alignment of the image",
    )
    title = blocks.CharBlock(max_length=60, help_text="60 characters max")
    text = blocks.TextBlock(max_length=140, required=False)
    link = GenericLink()

    class Meta:
        template = "stream_fields/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"


class CallToActionBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100, help_text="100 characters max.")
    subtitle = blocks.CharBlock(max_length=200, help_text="200 characters max.", required=False, blank=True, null=True)
    link = GenericLink()
    background_image = ImageChooserBlock()

    class Meta:
        icon = "plus"
        label = "Call to Action"
        template = "stream_fields/call_to_action_block.html"


class GenericFAQItem(blocks.StructBlock):
    asked_question = blocks.TextBlock(max_length=200, help_text="FAQ Question")
    answer = blocks.RichTextBlock(max_length=200, help_text="FAQ Answer")


class FAQBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100, help_text="100 characters max.")
    questions = blocks.ListBlock(GenericFAQItem())

    class Meta:
        # label = 'FAQ Section'
        template = "stream_fields/frequently_asked_questions.html"


class GenericProcessStep(blocks.StructBlock):
    step_title = blocks.CharBlock(
        max_length=100, help_text="Individual step title, 100 characters max."
    )
    step_description = blocks.TextBlock(
        max_length=200, help_text="A short desctiption of the step"
    )


class MultiStepProcessBlock(blocks.StructBlock):
    """A Block for showing the user a multi step process in hronological order"""

    title = blocks.CharBlock(
        max_length=100, help_text="Section title 100 characters max."
    )
    steps = blocks.ListBlock(GenericProcessStep())

    class Meta:
        template = "stream_fields/multi_step_block.html"



class NewsletterEmailCollectionBlock(blocks.StructBlock):
    '''Component containing a form for gathering newsletter emails'''
    title = blocks.CharBlock(
        max_length=200, help_text='Main title for this section (max 200 characters)'
    )
    subtitle = blocks.CharBlock(
        max_length=200, help_text="Subtitle for this section (max 200 characters)"
    )
    button_text = blocks.CharBlock(
        max_length=20, help_text="Text for the submit button",default="Subscribe"
    )
    disclaimer_text = blocks.CharBlock(
        max_length=200, help_text="Text disclaiming Terms and Conditions"
    )
    terms_and_conditions_link = GenericLink()


    class Meta:
        template = "stream_fields/news_letter_subscription_block.html"


class TimelineItem(blocks.StructBlock):
    marker_caption = blocks.CharBlock(
        max_length=50, help_text='Text for the left side marker of the timeline'
    )
    title_primary = blocks.CharBlock(
        max_length=50, help_text='Bold title on the right site of the timeline'
    )
    title_secondary = blocks.CharBlock(
        max_length=50, help_text='Cursive title above the primary title'
    )
    content =  blocks.CharBlock(
        max_length=300, help_text='Content describing the individual timeline item. max 300 characters.'
    )

    



class TimelineBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=200, help_text='Main title for this section (max 200 characters)'
    )
    subtitle = blocks.CharBlock(
        max_length=200, help_text='Optional subtitle, (max 200 characters)'
    )
    items = blocks.ListBlock(TimelineItem())

    class Meta:
        template = 'stream_fields/timeline_block.html'


class WhyUsCard(blocks.StructBlock):
    icon = ImageChooserBlock(required=False,help_text='Icon to be displayed in a card, will be downscaled for performance.')
    title = blocks.CharBlock(
        max_length=200, help_text='Main title for this section (max 200 characters).'
    )
    content = blocks.CharBlock(
        max_length=200, help_text='A short description of the card.'
    )



class WhyUsBlock(blocks.StructBlock):
    pill_caption = blocks.CharBlock(
        max_length=50, help_text='Main title for this section (max 50 characters).'
    )
    title = blocks.CharBlock(
        max_length=200, help_text='Main title for this section (max 200 characters).'
    )
    subtitle = blocks.CharBlock(
        max_length=200, help_text='Optional subtitle, (max 200 characters).'
    )

    featured_cards = blocks.ListBlock(WhyUsCard())

    class Meta:
        template = 'stream_fields/why_us_block.html'

class FreeProductCard(blocks.StructBlock):
    card_image = ImageChooserBlock(help_text='Background image for the card, will be overlayed by text.')
    product_link = GenericLink()
    title = blocks.CharBlock(
        max_length=200, help_text='Main title for this section (max 200 characters).'
    )
    content = blocks.CharBlock(
        max_length=200, help_text='Main content for the card (max 200 characters).'
    )

class FeaturedFreeProductBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=200, help_text='Main title for this section (max 200 characters).'
    )
    subtitle = blocks.CharBlock(
        max_length=200, help_text='Optional subtitle, (max 200 characters).'
    )
    free_product_cards = blocks.ListBlock(FreeProductCard())

    class Meta:
        template = 'stream_fields/free_products_block.html'
