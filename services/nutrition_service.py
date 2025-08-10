import requests
from config import CALORIES_NINJA_KEY

def get_nutrition(food_name):
    """Fetch nutrition info from CaloriesNinjas."""
    url = f"https://api.calorieninjas.com/v1/nutrition?query={food_name}"
    headers = {"X-Api-Key": CALORIES_NINJA_KEY}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()
        if data["items"]:
            return data["items"][0]
    return None
