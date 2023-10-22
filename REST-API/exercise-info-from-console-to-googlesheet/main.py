"""
In this project, we will:
    1- Prompt the user to input the exercises they completed today.
    2- Collect the user's input and make a POST request to update their details on 'nutritionix.com' - which offers an NLP tool for nutrition information.
    3- After retrieving and formatting the exercise data, we will integrate it into a Google Sheet using 'Sheety' - an API that connects to your Google Sheet account.

Example in the png files in this folder.
"""

from secret_vars import NUTRITION_APP_ID, NUTRITION_API_KEY
import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 52
HEIGHT_CM = 163
AGE = 24

# ask the user what exercises they did today.
exercise_text = input("Wich exercises you did today?: ")

# convert the exercise text to formatted data into a dictionary (named "result").
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()

# add the data as a row in google sheet using 'sheety'.
curremt_date = datetime.now().strftime("%d.%m.%Y")
curremt_time = datetime.now().strftime("%H:%M")

sheety_endpoint = "https://api.sheety.co/8836c7947462e4e84ce2fea8bf8905c8/myWorkouts/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": curremt_date,
            "time": curremt_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs)
sheety_response.raise_for_status()

print("Your data updated. Go to your google sheet and see it!")