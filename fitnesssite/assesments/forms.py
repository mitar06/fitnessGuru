from django import forms
from . import widgets as custom_widgets
from . import renderers

class BaselineAssesmentForm(forms.Form):
    ''' Used for validating and saving data for 
        assesing clients current fitness level
        across multiple catagories of questions
    '''
    default_renderer = renderers.FGAssesmentFormRenderer

    PHYSICAL_ACTIVITIES = (
        ('Weightlifting', 'Weightlifting'),
        ('Running' , 'Running'),
        ('Yoga', 'Yoga'),
        ('Cycling', 'Cycling'),
        ('Swimming', 'Swimming'),
        ('Other', 'Other'),
    )
    TRANING_HOURS_PER_WEEK = (
        ('1-5', 'Less than 5'),
        ('5-10', '5 to 10'),
        ('11-15', '11 to 15'),
        ('15-99', 'More than 15'),
        ('0', "I don't train")
    )
    FITNESS_GOALS = (
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('endurance', "Endurance"),
        ('general_health', 'General Health')
    )

    EATING_HABITS_LEVEL = (
        ('0', 'Poor'),
        ('1', 'Average'),
        ('2', 'Good'),
        ('3', 'Excelent')
    )

    MEAL_FREQUENCIES = (
        ('small_frequent', 'Small and Frequent'),
        ('large_less_frequent', 'Larger, less Frequent'),
        ('no_preference', 'No Preference'),
    )
    ENERGY_LEVEL_SLUMPS = (
        ('never', "Never"),
        ('sometimes', 'Sometimes'),
        ('often', 'Often'),
        ('always', 'Always'),
    )

    STRESS_MANAGEMENT = (
        ('0', 'Physical Exercise'),
        ('1', 'Mindfullness nad meditation'),
        ('2', 'Creative Outlets'),
        ('3', 'Social Support'),
        ('4', 'Relaxation Techniques'),
        ('5', 'Other'),

    )
    WORKOUT_FREQUECY = (
        ('0', 'Minimal Physical Activity'),
        ('1', 'Regular Walks'),
        ('2', 'Exercise 1-2 times per week'),
        ('3','Exercise 3-5 days per week'),
        ('4', 'Exercise 5-7 days per week'),
    )

    MEAT_PREFERENCES = (
       ('fish', 'Fish'),
       ('chicken', 'Chicken'),
       ('turkey', 'Turkey'),
       ('pork', 'Pork'),
       ('beef', 'Beef')
    )
    VEGETABLE_PREFERENCES = (
        ('potato', 'Potatoes'),
        ('broccoli', 'Broccoli'),
        ('cabbage', 'Cabbage'),
        ('carrots', 'Carrots'),
        ('peppers', 'Bell Peppers')
    )
    CARB_PREFERENCES = (
        ('rice', 'Rice'),
        ('quinoua', 'Quinoua'),
        ('cheick_peas','Chick Peas'),
        ('lentils', 'Lentils')
    )
    favorite_activity = forms.ChoiceField(
        choices=PHYSICAL_ACTIVITIES,
        label='What is your primary sport or physical activity?',
        widget=custom_widgets.FGRadioSelect(attrs={
            'class' : 'flex flex-col gap-y-2',
            "x-model" : 'favorite_activity',
            'decorative_title' : "What is your primary sport or physical activity?",
            'decorative_subtitle' : "Choose Your Main Sporting Activity",
            'decorative_image' : 'images/workout.png',
            }),
        required=True,  
    )
    weekly_training_hours = forms.ChoiceField(
        choices=TRANING_HOURS_PER_WEEK,
        label='How many Hours per week do you train?',
        widget=custom_widgets.FGRadioSelect(attrs={
            'class' : 'flex flex-col gap-y-2', 
            "x-model" : 'weekly_training_hours',
            'decorative_title' : "How Many Hours Per Week Do you train?",
            'decorative_subtitle' : "Finding out more about your training intensity",
            'decorative_image' : 'images/rapQrPeSQ0EPtaZJV3OCJoNub85qAGVxxjaa5mFD.webp',
            }),
        required=True,  
    )

    main_fitness_goal = forms.ChoiceField(
        choices=FITNESS_GOALS,
        label = 'What is you primary Fitness Goal?',
        widget=custom_widgets.FGRadioSelect(attrs={
            'class' : 'flex flex-col gap-y-2',
            "x-model" : 'main_fitness_goal',
            'decorative_title' : "What is your primary sport or physical activity?",
            'decorative_subtitle' : "Choose Your Main Sporting Activity",
            'decorative_image' : 'images/workout.png',
            }
            )
    )

    eating_habits_level = forms.ChoiceField(
        choices=EATING_HABITS_LEVEL,
        label="How do you rate your current eating habits?",
        widget=custom_widgets.FGRadioSelect(attrs={'class' : 'flex flex-col gap-y-2', "x-model" : 'eating_habits_level'})
    )
    preferred_meal_frequency = forms.ChoiceField(
        choices=MEAL_FREQUENCIES,
        label="Do you prefer to eat smaller meals more frequently or larger meals less often?",
        widget=custom_widgets.FGRadioSelect(attrs={'class' : 'flex flex-col gap-y-2', "x-model" : 'preferred_meal_frequency'})
    )
    energy_level_slumps = forms.ChoiceField(
        choices=ENERGY_LEVEL_SLUMPS,
        label="Do you experience energy slumps during the day?",
        widget=custom_widgets.FGRadioSelect(attrs={'class' : 'flex flex-col gap-y-2', "x-model" : 'preferred_meal_frequency'})
    )
    sleep_quality = forms.ChoiceField(
        choices=EATING_HABITS_LEVEL,
        label="How do you rate your sleep quality?",
        widget=custom_widgets.FGRadioSelect(attrs={'class' : 'flex flex-col gap-y-2', "x-model" : 'sleep_quality'})
    )
    
    stress_management_style = forms.ChoiceField(
        choices=STRESS_MANAGEMENT,
        label="What's Your Approach to Handling Stress?",
        widget=custom_widgets.FGRadioSelect(attrs={'class' : 'flex flex-col gap-y-2', "x-model" : 'stress_management_style'})
    )



    meat_preferences = forms.ChoiceField(
        choices=MEAT_PREFERENCES,
        label = 'What meats would you like to be included in your meal plan.',
        widget=custom_widgets.FGCheckboxSelectMultiple(attrs={'class' : 'flex flex-col gap-y-2', "x-model" : 'meat_preferences'})
    )

    vegetable_preferences = forms.ChoiceField(
        choices=VEGETABLE_PREFERENCES,
        label = 'What vegetables would you like to be included in your meal plan.',
        widget=custom_widgets.FGCheckboxSelectMultiple(attrs={'class' : 'flex flex-col gap-y-2', "x-model" : 'vegetable_preferences'})
    )