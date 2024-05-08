from django import forms
import assesments.widgets as custom_widgets


class ImperialHeightAndWeightField(forms.fields.MultiValueField):

    widget = custom_widgets.FGHeightWeightMultiWidget

    def __init__(self, required=False, widget=None, label=None, initial=None):
        fields = (
            forms.FloatField(label="Height in feet"),
            forms.FloatField(label="Height in Inches"),
        )
        super(ImperialHeightAndWeightField, self).__init__(fields)

    def decompress(self, value):
        print(value)
        if value:
            data = value
            return [data[0], data[1]]
        return [None, None, None]

    def compress(self, data_list):

        return data_list
