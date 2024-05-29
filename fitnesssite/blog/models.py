from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks as baseBlocks
from stream_fields import blocks
from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from wagtail.snippets.models import register_snippet

from django.shortcuts import reverse


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)
    short_description = models.TextField(
        verbose_name="Short Description",
        max_length=250,
        blank=True,
        null=True,
        help_text="A short description of the category, max. 250 characters.",
    )
    category_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name="Category Image",
        blank=True,
        null=True,
        help_text="Category Image to display as a thumbnail (resized to 150x150).",
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
        FieldPanel("category_image"),
        FieldPanel("short_description"),
    ]

    def get_category_ulr(self):
        """Currently rediredct to all posts with
        category slug in the query string

        """
        return f"/blog?filtered_category={self.slug}"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


# Create your models here.


class PostPageBlogCategory(models.Model):
    page = ParentalKey(
        "blog.BlogDetailPage", on_delete=models.CASCADE, related_name="categories"
    )
    blog_category = models.ForeignKey(
        "blog.BlogCategory", on_delete=models.CASCADE, related_name="post_pages"
    )

    panels = [
        FieldPanel("blog_category"),
    ]

    class Meta:
        unique_together = ("page", "blog_category")


class CategoryIndexPage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["categories"] = BlogCategory.objects.all()
        return context


class BlogIndexPage(Page):
    custom_title = models.CharField(
        max_length=100, blank=False, null=False, help_text="Overrides Wagtail title."
    )
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        posts = BlogDetailPage.objects.live().public().prefetch_related("categories")

        tag = request.GET.get("tag")
        category = request.GET.get("category")

        if tag:
            posts = posts.filter(tags__name=tag)
            context["current_tag"] = tag

        if category:
            try:
                categoryObject = BlogCategory.objects.filter(
                    slug__exact=category
                ).first()
                posts = posts.filter(categories__blog_category=categoryObject)
            except BlogCategory.DoesNotExist as e:
                context["filtered_category"] = None
            context["filtered_category"] = categoryObject.name
        context["posts"] = posts
        return context


class BlogPageTag(TaggedItemBase):

    content_object = ParentalKey(
        "blog.BlogDetailPage", on_delete=models.CASCADE, related_name="tagged_items"
    )


class BlogDetailPage(Page):

    def get_absolute_url(self, request=None):

        possible_sites = [
            (pk, path, url, language_code)
            for pk, path, url, language_code in self._get_site_root_paths(request)
            if self.url_path.startswith(path)
        ]

        if not possible_sites:
            return None

        site_id, root_path, root_url, language_code = possible_sites[0]

        return reverse("wagtail_serve", args=(self.url_path[len(root_path) :],))

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    custom_title = models.CharField(
        max_length=100, blank=False, null=False, help_text="Overrides Wagtail title."
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content = StreamField(
        [
            ("title", blocks.TitleBlock()),
            ("cards", blocks.CardsListBlock()),
            ("image_and_text", blocks.ImageAndTextBlock()),
            ("call_to_action", blocks.CallToActionBlock()),
            ("frequently_asked_questions", blocks.FAQBlock()),
            ("multi_step", blocks.MultiStepProcessBlock()),
            ("rich_text", baseBlocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        InlinePanel("categories", label="category"),
        FieldPanel("custom_title"),
        FieldPanel("banner_image"),
        FieldPanel("content"),
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel("tags"),
    ]
