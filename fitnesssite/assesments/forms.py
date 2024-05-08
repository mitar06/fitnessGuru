from django import forms
from . import widgets as custom_widgets
from . import renderers

from . import fields as custom_fields
from .utils import convert_body_measuremtns_to_metric_dict


class BaselineAssesmentForm(forms.Form):
    """Used for validating and saving data for
    assesing clients current fitness level
    across multiple catagories of questions
    """

    default_renderer = renderers.FGAssesmentFormRenderer

    PHYSICAL_ACTIVITIES = (
        ("Weightlifting", "Weightlifting"),
        ("Running", "Running"),
        ("Yoga", "Yoga"),
        ("Cycling", "Cycling"),
        ("Swimming", "Swimming"),
        ("Other", "Other"),
    )
    TRANING_HOURS_PER_WEEK = (
        ("1-5", "Less than 5"),
        ("5-10", "5 to 10"),
        ("11-15", "11 to 15"),
        ("15-99", "More than 15"),
        ("0", "I don't train"),
    )
    FITNESS_GOALS = (
        ("weight_loss", "Weight Loss"),
        ("muscle_gain", "Muscle Gain"),
        ("endurance", "Endurance"),
        ("general_health", "General Health"),
    )

    EATING_HABITS_LEVEL = (
        ("0", "Poor"),
        ("1", "Average"),
        ("2", "Good"),
        ("3", "Excelent"),
    )

    MEAL_FREQUENCIES = (
        ("small_frequent", "Small and Frequent"),
        ("large_less_frequent", "Larger, less Frequent"),
        ("no_preference", "No Preference"),
    )
    ENERGY_LEVEL_SLUMPS = (
        ("never", "Never"),
        ("sometimes", "Sometimes"),
        ("often", "Often"),
        ("always", "Always"),
    )

    STRESS_MANAGEMENT = (
        ("0", "Physical Exercise"),
        ("1", "Mindfullness nad meditation"),
        ("2", "Creative Outlets"),
        ("3", "Social Support"),
        ("4", "Relaxation Techniques"),
        ("5", "Other"),
    )
    WORKOUT_FREQUECY = (
        ("0", "Minimal Physical Activity"),
        ("1", "Regular Walks"),
        ("2", "Exercise 1-2 times per week"),
        ("3", "Exercise 3-5 days per week"),
        ("4", "Exercise 5-7 days per week"),
    )

    MEAT_PREFERENCES = [
        ("fish", "Fish"),
        ("chicken", "Chicken"),
        ("turkey", "Turkey"),
        ("pork", "Pork"),
        ("beef", "Beef"),
    ]
    VEGETABLE_PREFERENCES = [
        ("potato", "Potatoes"),
        ("broccoli", "Broccoli"),
        ("cabbage", "Cabbage"),
        ("carrots", "Carrots"),
        ("peppers", "Bell Peppers"),
    ]
    CARB_PREFERENCES = (
        ("rice", "Rice"),
        ("quinoua", "Quinoua"),
        ("cheick_peas", "Chick Peas"),
        ("lentils", "Lentils"),
    )
    favorite_activity = forms.ChoiceField(
        choices=PHYSICAL_ACTIVITIES,
        label="What is your primary sport or physical activity?",
        widget=custom_widgets.FGRadioSelect(
            attrs={
                "class": "flex flex-col gap-y-2",
                "x-model": "favorite_activity",
                "decorative_title": "What is your primary sport or physical activity?",
                "decorative_subtitle": "Choose Your Main Sporting Activity",
                "decorative_image": "images/workout.png",
            }
        ),
        required=True,
    )
    workout_frequency = forms.ChoiceField(
        choices=WORKOUT_FREQUECY,
        label="How Many Hours per week do you train",
        widget=custom_widgets.FGRadioSelect(
            attrs={
                "class": "flex flex-col gap-y-2",
                "x-model": "workout_frequency",
                "decorative_title": "What is your physical activity level?",
                "decorative_subtitle": "Getting to know your current habits.",
                "decorative_image": "images/rapQrPeSQ0EPtaZJV3OCJoNub85qAGVxxjaa5mFD.webp",
            }
        ),
    )
    weekly_training_hours = forms.ChoiceField(
        choices=TRANING_HOURS_PER_WEEK,
        label="How many Hours per week do you train?",
        widget=custom_widgets.FGRadioSelect(
            attrs={
                "class": "flex flex-col gap-y-2",
                "x-model": "weekly_training_hours",
                "decorative_title": "How Many Hours Per Week Do you train?",
                "decorative_subtitle": "Finding out more about your training intensity",
                "decorative_image": "images/rapQrPeSQ0EPtaZJV3OCJoNub85qAGVxxjaa5mFD.webp",
            }
        ),
        required=True,
    )

    main_fitness_goal = forms.ChoiceField(
        choices=FITNESS_GOALS,
        label="What is you primary Fitness Goal?",
        widget=custom_widgets.FGRadioSelect(
            attrs={
                "class": "flex flex-col gap-y-2",
                "x-model": "main_fitness_goal",
                "decorative_title": "What is your primary sport or physical activity?",
                "decorative_subtitle": "Choose Your Main Sporting Activity",
                "decorative_image": "images/workout.png",
            }
        ),
    )

    eating_habits_level = forms.ChoiceField(
        choices=EATING_HABITS_LEVEL,
        label="How do you rate your current eating habits?",
        widget=custom_widgets.FGRadioSelect(
            attrs={
                "class": "flex flex-col gap-y-2",
                "x-model": "eating_habits_level",
                "decorative_title": "How do you rate your current eating habits?",
                "decorative_subtitle": "Getting to know your eating patterns",
                "decorative_image": "images/MealFrequency.webp",
            }
        ),
    )
    preferred_meal_frequency = forms.ChoiceField(
        choices=MEAL_FREQUENCIES,
        label="Do you prefer to eat smaller meals more frequently or larger meals less often?",
        widget=custom_widgets.FGRadioSelect(
            attrs={
                "class": "flex flex-col gap-y-2",
                "x-model": "preferred_meal_frequency",
                "decorative_title": "Do you prefer to eat smaller meals more frequently or larger meals less often?",
                "decorative_subtitle": "",
                "decorative_image": "images/MealSize.webp",
            }
        ),
    )
    energy_level_slumps = forms.ChoiceField(
        choices=ENERGY_LEVEL_SLUMPS,
        label="Do you experience energy slumps during the day?",
        widget=custom_widgets.FGRadioSelect(
            attrs={
                "class": "flex flex-col gap-y-2",
                "x-model": "energy_level_slumps",
                "decorative_title": "Do you experience energy slumps during the day?",
                "decorative_subtitle": "",
                "decorative_image": "images/EnergySlumps.webp",
            }
        ),
    )
    sleep_quality = forms.ChoiceField(
        choices=EATING_HABITS_LEVEL,
        label="How do you rate your sleep quality?",
        widget=custom_widgets.FGRadioSelect(
            attrs={
                "class": "flex flex-col gap-y-2",
                "x-model": "sleep_quality",
                "decorative_title": "How do you rate your sleep quality?",
                "decorative_subtitle": "",
                "decorative_image": "images/sleepQuality.webp",
            }
        ),
    )

    stress_management_style = forms.ChoiceField(
        choices=STRESS_MANAGEMENT,
        label="What's Your Approach to Handling Stress?",
        widget=custom_widgets.FGRadioSelect(
            attrs={
                "class": "flex flex-col gap-y-2",
                "x-model": "stress_management_style",
                "decorative_title": "What is your favorite way to handle stress",
                "decorative_subtitle": "",
                "decorative_image": "images/stressManagement.webp",
            }
        ),
    )

    meat_preferences = forms.MultipleChoiceField(
        choices=MEAT_PREFERENCES,
        label="What meats would you like to be included in your meal plan.",
        widget=custom_widgets.FGCheckboxSelectMultiple(
            attrs={
                "class": "flex flex-col gap-y-2",
                "x-model": "meat_preferences",
                "decorative_title": "What meats would you like to have included in the plan?",
                "decorative_subtitle": "",
                "decorative_image": "images/meatPreferences.webp",
            }
        ),
    )

    vegetable_preferences = forms.MultipleChoiceField(
        choices=VEGETABLE_PREFERENCES,
        label="What vegetables would you like to be included in your meal plan.",
        widget=custom_widgets.FGCheckboxSelectMultiple(
            attrs={
                "class": "flex flex-col gap-y-2",
                "x-model": "vegetable_preferences",
                "decorative_title": "What vegetables would you like to have included in the plan?",
                "decorative_subtitle": "",
                "decorative_image": "images/vegetablePreferences.webp",
            }
        ),
    )


class MetricBodyMeasurementsForm(forms.Form):

    weight_kg = forms.FloatField(
        max_value=200,
        label="Weight",
        widget=custom_widgets.FGNumberInput(
            attrs={
                "label": "Your Weight",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        ),
    )
    target_weight_kg = forms.FloatField(
        max_value=200,
        widget=custom_widgets.FGNumberInput(
            attrs={
                "label": "Your Target Weight",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        ),
    )
    height_cm = forms.FloatField(
        max_value=230,
        label="Height",
        widget=custom_widgets.FGNumberInput(
            attrs={
                "label": "Your Height in cm.",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        ),
    )
    age = forms.IntegerField(
        max_value=100,
        min_value=15,
        label="Your Age",
        widget=custom_widgets.FGNumberInput(
            attrs={
                "label": "Your Age",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        ),
    )


class ImperialBodyMeasurementsForm(forms.Form):
    weight = forms.FloatField(
        max_value=450,
        label="Weight in lbs",
        widget=custom_widgets.FGNumberInput(
            attrs={
                "label": "Your Weight",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        ),
    )
    target_weight = forms.FloatField(
        max_value=450,
        widget=custom_widgets.FGNumberInput(
            attrs={
                "label": "Your Target Weight",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        ),
    )
    height = custom_fields.ImperialHeightAndWeightField(
        widget=custom_widgets.FGHeightWeightMultiWidget()
    )

    age = forms.IntegerField(
        max_value=100,
        min_value=15,
        label="Your Age",
        widget=custom_widgets.FGNumberInput(
            attrs={
                "label": "Your Age",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        ),
    )

    def clean(self):
        """
        We are converting height to the metric system in order to store it in the model correctly
        """
        self.cleaned_data = super(ImperialBodyMeasurementsForm, self).clean()
        if len(self.cleaned_data.get("height", [])) == 2:
            (height_ft, height_in) = self.cleaned_data.get("height", None)
            self.cleaned_data = convert_body_measuremtns_to_metric_dict(
                self.cleaned_data["weight"],
                self.cleaned_data["target_weight"],
                height_ft,
                height_in,
                self.cleaned_data["age"],
            )

        return self.cleaned_data
