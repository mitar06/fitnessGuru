import calendar
from django.shortcuts import (
    render,
    redirect,
)

from .utils import (
    calculate_bmi,
    calaulate_bmr,
    calculate_daily_water_intake,
    get_bmi_bracket,
)

import uuid

from django.utils import timezone
from django.db import transaction
from .forms import (
    BaselineAssesmentForm,
    MetricBodyMeasurementsForm,
    ImperialBodyMeasurementsForm,
)

from .models import FitnessAssesmentProfile


def assesment_admin(request):

    submissions = FitnessAssesmentProfile.objects.all()

    return render(
        request,
        "assesments/admin.html",
        {
            "submissions": submissions,
        },
    )


def index(request):

    if request.method == "POST":
        body_measurements_processed = False
        body_measurement_data = dict()
        form = BaselineAssesmentForm(request.POST)
        metric_measurements = MetricBodyMeasurementsForm(request.POST)
        imperial_measurements = ImperialBodyMeasurementsForm(request.POST)

        if imperial_measurements.is_valid() and not body_measurements_processed:
            body_measurement_data = imperial_measurements.cleaned_data
            body_measurements_processed = True

        if metric_measurements.is_valid() and not body_measurements_processed:
            body_measurement_data = metric_measurements.cleaned_data

        if form.is_valid():
            temporary_uuid = request.COOKIES.get("assesment_customer_uuid")
            customer_data = form.cleaned_data
            customer_data.pop("meat_preferences")
            customer_data.pop("vegetable_preferences")
            full_assesment_data = form.cleaned_data
            if body_measurement_data:
                full_assesment_data = {**full_assesment_data, **body_measurement_data}
                print(full_assesment_data)

            with transaction.atomic():
                obj = FitnessAssesmentProfile.objects.create(
                    **full_assesment_data,
                )
                obj.customer_uuid = temporary_uuid
                obj.save()

            return redirect(
                "assesments:results",
                customer_uuid=request.COOKIES.get("assesment_customer_uuid"),
            )

        else:

            return render(request, "assesments/index.html", {"form": form})
    else:
        form = BaselineAssesmentForm()
        measurements_metric_form = MetricBodyMeasurementsForm()
        measurements_imperial_form = ImperialBodyMeasurementsForm()

        response = render(
            request,
            "assesments/index.html",
            {
                "form": form,
                "measurements_metric": measurements_metric_form,
                "measurements_imperial": measurements_imperial_form,
            },
        )
        if not request.COOKIES.get("assesment_customer_uuid"):
            response.set_cookie("assesment_customer_uuid", uuid.uuid4())
        return response


def post_assesment_preview_dashboard(request, customer_uuid):

    customer_profile = FitnessAssesmentProfile.objects.filter(
        customer_uuid=customer_uuid
    ).first()

    body_mass_index = calculate_bmi(
        customer_profile.height_cm, customer_profile.weight_kg
    )
    bmi_bracket_label = get_bmi_bracket(body_mass_index)
    basal_metabolic_rate = calaulate_bmr(
        customer_profile.height_cm, customer_profile.weight_kg, customer_profile.age
    )

    daily_water_intake = calculate_daily_water_intake(customer_profile.weight_kg)

    context_data = {
        "age": customer_profile.age,
        "weight": customer_profile.weight_kg,
        "height": customer_profile.height_cm,
        "target_weight": customer_profile.target_weight_kg,
        "bmi": body_mass_index,
        "bmi_label": bmi_bracket_label,
        "bmr": basal_metabolic_rate,
        "water_intake": round(daily_water_intake, 1),
    }

    return render(
        request, "assesments/post_assesment_dashboard.html", {"data": context_data}
    )
