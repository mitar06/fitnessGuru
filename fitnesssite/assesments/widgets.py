from django.forms.widgets import (
    RadioSelect,
    CheckboxSelectMultiple,
    NumberInput,
    MultiWidget,
)


class FGRadioSelect(RadioSelect):
    template_name = "assesments/widget/fg_radio_select.html"
    option_template_name = "assesments/widget/fg_radio_option.html"


class FGCheckboxSelectMultiple(CheckboxSelectMultiple):
    template_name = "assesments/widget/fg_checkbox_select_multiple.html"
    option_template_name = "assesments/widget/fg_checkbox_option.html"


class FGNumberInput(NumberInput):
    """
    A Tailwind Styled number input with label

    """

    template_name = "assesments/widget/fg_measurement_number_input.html"


class FGHeightWeightMultiWidget(MultiWidget):
    """Used for displaying height and weight in feet and inches"""

    template_name = "assesments/widget/fg_height_weight_multi_widget.html"

    def __init__(self, attrs=None):
        widgets = {
            "ft": FGNumberInput(
                attrs={
                    "label": "Height in feet",
                    "name": "height_ft",
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
            "in": FGNumberInput(
                attrs={
                    "label": "Height in inches",
                    "name": "height_in",
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
        }

        super(FGHeightWeightMultiWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        print(value)
        if value:
            return [value, value]
        return [None, None]
