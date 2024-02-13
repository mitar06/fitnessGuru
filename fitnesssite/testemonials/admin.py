from wagtail_modeladmin.options import ModelAdmin, modeladmin_register

from .models import Testemonial


@modeladmin_register
class TestemonialAdmin(ModelAdmin):
    """Model Admin for Testemonial"""

    model = Testemonial
    menu_label = "Testemonials"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("body", "attribution")
    # search_fields = ''
