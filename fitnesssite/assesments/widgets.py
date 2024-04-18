from django.forms.widgets import (
    RadioSelect,
    CheckboxSelectMultiple,
)


class FGRadioSelect(RadioSelect):
    template_name =  'assesments/widget/fg_radio_select.html'
    option_template_name = 'assesments/widget/fg_radio_option.html'




class FGCheckboxSelectMultiple(CheckboxSelectMultiple):
    template_name =  'assesments/widget/fg_checkbox_select_multiple.html'
    option_template_name = 'assesments/widget/fg_checkbox_option.html'