from django.forms.renderers import DjangoTemplates, EngineMixin


class FGAssesmentFormRenderer(DjangoTemplates):

    form_template_name = "assesments/forms/fg_assesment_form.html"
