from django.db import models

from django.contrib.auth import get_user_model


user_model = get_user_model()


# Create your models here.
class FitnessAssesmentProfile(models.Model):
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

    customer_uuid = models.UUIDField(null=True)
    workout_frequency = models.CharField(
        max_length=200, choices=WORKOUT_FREQUECY, default="1"
    )
    favorite_activity = models.CharField(max_length=200, choices=PHYSICAL_ACTIVITIES)
    weekly_training_hours = models.CharField(
        max_length=200, choices=TRANING_HOURS_PER_WEEK
    )
    main_fitness_goal = models.CharField(max_length=200, choices=FITNESS_GOALS)
    eating_habits_level = models.CharField(max_length=200, choices=EATING_HABITS_LEVEL)
    preferred_meal_frequency = models.CharField(
        max_length=200, choices=MEAL_FREQUENCIES
    )
    energy_level_slumps = models.CharField(max_length=200, choices=ENERGY_LEVEL_SLUMPS)
    sleep_quality = models.CharField(max_length=200, choices=EATING_HABITS_LEVEL)
    stress_management_style = models.CharField(
        max_length=200, choices=STRESS_MANAGEMENT
    )
    height_cm = models.DecimalField(
        verbose_name="Height(cm)", decimal_places=1, max_digits=4, null=True
    )
    weight_kg = models.DecimalField(
        verbose_name="Weight(kg)", decimal_places=1, max_digits=4, null=True
    )
    target_weight_kg = models.DecimalField(
        verbose_name="Target Weight (kg)", decimal_places=1, max_digits=4, null=True
    )
    age = models.DecimalField(
        verbose_name="Age", decimal_places=0, max_digits=2, null=True
    )

    def convert_body_measurements_to_imperial(self):
        """Returns body measurements in imperial format
        :param self
        :rtype: tuple
        :return (height_ft, height_in, weight_lbs, target_weight_lbs, age,)
        """
        feet = 0.3937 * self.height_cm
        inches = 0.0328 * self.height_cm
        weight_lbs = self.weight_kg * 2.205
        target_weight_lbs = self.target_weight_kg * 2.205

        return (feet, inches, weight_lbs, target_weight_lbs, self.age)
