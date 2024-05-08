from wagtail import hooks

from .views import assesment_admin
from django.urls import path, reverse

from wagtail.admin.menu import MenuItem


@hooks.register("register_admin_urls")
def register_calendar_url():
    return [
        path("asessments/", assesment_admin, name="asessments"),
    ]


@hooks.register("register_admin_menu_item")
def register_calendar_menu_item():
    return MenuItem("Assesments", reverse("asessments"), icon_name="date")
