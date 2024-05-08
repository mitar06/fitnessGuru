from django.urls import path
from . import views

app_name = "assesments"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "results/<uuid:customer_uuid>",
        views.post_assesment_preview_dashboard,
        name="results",
    ),
]
