from django.apps import AppConfig
from django_comments.signals import comment_was_posted

from django.core.cache.utils import make_template_fragment_key
from django.core.cache import cache


def callback(sender, **kwargs):

    page_id = kwargs["comment"]["object_pk"]
    cache_key_to_clear = make_template_fragment_key("comment_tree", vary_on=[page_id])
    cache.delete(cache_key_to_clear)


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

    def ready(self):
        comment_was_posted.connect(callback)
