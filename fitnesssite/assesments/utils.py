from decimal import Decimal
from typing import Dict
import numbers


def convert_body_measuremtns_to_metric_dict(
    weight_lbs: Decimal,
    target_weight_lbs: Decimal,
    height_ft: Decimal,
    height_in: Decimal,
    age: Decimal,
) -> Dict[str, Decimal]:
    """
    Takes body measurement data in the imperial system, converts the values
     and returns a disc with metric system representations of those measurements

    """

    weight_kg = round(weight_lbs * 0.45, 1)
    target_weight_kg = round(target_weight_lbs * 0.45, 1)
    height_cm = round(height_ft * 31, 2) + round(height_in * 2.45, 2)

    return {
        "height_cm": height_cm,
        "weight_kg": weight_kg,
        "target_weight_kg": target_weight_kg,
        "age": age,
    }


def calculate_bmi(height_cm: Decimal, weight_kg: Decimal) -> float:

    if height_cm and weight_kg:
        return round(weight_kg / (height_cm / 100) ** 2, 1)
    return 0

def get_bmi_bracket(bmi: Decimal) -> str:
    '''Takes in a person's BMI and returns a BMI bracket
        Brackets include:
        Underweight
        Healthy Range
        Overweight
        Obese
        Severely Obese
    '''
    if not bmi:
        raise ValueError('Plase provide a valid bmi value to this method')

    if bmi < 18.5:
        return "Underweight"
    if 19 < bmi <= 24.9:
        return "Healthy Range"
    if 25 <= bmi <= 29.9:
        return "Overweight"
    if 30 <= bmi <= 39.9:
        return "Obese"
    if bmi >= 40:
        return "Severely Obese"


def calaulate_bmr(
    height_cm: Decimal, weight_kg: Decimal, age: Decimal, is_male=True
) -> Decimal:
    if not (height_cm and weight_kg and age):
        return 0
    if is_male:
        return round(
            (
                Decimal(66.5)
                + (Decimal(13.75) * weight_kg)
                + (Decimal(5) * height_cm)
                - (Decimal(6.755) * age)
            )
            * Decimal(1.2),
            2,
        )
    else:
        return round(
            Decimal(655.1)
            + (Decimal(9.6) * weight_kg)
            + (Decimal(1.8) * height_cm)
            - (Decimal(6.755) * age),
            2,
        )


def calculate_metabolic_age(height_cm, weight_kg, age, is_male=True):
    '''
    Still need to research for a good source of BMI data per age bracket
    '''
    pass

def calculate_daily_water_intake(weight_kg: Decimal) -> Decimal:
    '''
    Takes in a persons weight in kg 
    @param : weight_kg Decimal

    @returns: recommended daily water intake in liters
    
    '''

    if not weight_kg:
        raise ValueError('Please supply a weight in kilograms!')

    if not isinstance(weight_kg, numbers.Number):
        raise ValueError(f"{weight_kg} is not a number.")
    
    return weight_kg * Decimal(0.03)
