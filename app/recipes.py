# this is the app/recipes.py file...

# LOCAL DEV (ENV VARS)

import requests
import json
import os

from dotenv import load_dotenv

load_dotenv() # looks in the ".env" file for env vars

API_KEY = os.getenv("SPOONACULAR_API_KEY", default="demo")

def retrieve_recipes_by_ingredients(search_criteria, cuisine, diet, intolerances, dish_type, maxReadyTime, sort, number, fillIngredients):

    url_parameters = {"search_criteria":search_criteria,"cuisine":cuisine,"diet":diet,"intolerances":intolerances,"type":dish_type,"maxReadyTime":maxReadyTime,"sort":sort,"number":number,"fillIngredients":fillIngredients}
    selected_url_parameters = ""

    for key in url_parameters:
        if key in url_parameters and url_parameters[key] is not None:
          selected_url_parameters += f"{key}={url_parameters[key]}&"

    request_url = f"https://api.spoonacular.com/recipes/complexSearch?{selected_url_parameters}apiKey={API_KEY}"

    response = requests.get(request_url)

    parsed_response = json.loads(response.text)
    
    data = parsed_response["results"]

    return data

def retrieve_recipes_by_keyword(search_criteria, diet, intolerances, number, fillIngredients):

    url_parameters = {"query":search_criteria,"diet":diet,"intolerances":intolerances,"number":number,"fillIngredients":fillIngredients}
    selected_url_parameters = ""

    for key in url_parameters:
        if key in url_parameters and url_parameters[key] is not None:
          selected_url_parameters += f"{key}={url_parameters[key]}&"

    request_url = f"https://api.spoonacular.com/recipes/complexSearch?{selected_url_parameters}apiKey={API_KEY}"

    response = requests.get(request_url)

    parsed_response = json.loads(response.text)
    
    data = parsed_response["results"]

    return data

def retrieve_recipe_info(recipe_id):

    request_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}"

    response = requests.get(request_url)

    parsed_response = json.loads(response.text)
  
    return parsed_response


if __name__ == "__main__":

    selected_search_criteria = ["apples","flour","sugar"]
    selected_cuisine = None # Type of food (ex., "Italian")--dropdown list
    selected_diet = None # Special diets (ex., "vegetarian")--dropdown list
    selected_intolerances = None # Dietary resrictions (ex., "gluten")--dropdown list
    selected_dish_type = None # Type of dish (ex., "main course")--dropdown list
    selected_maxReadyTime = None # Denoted in minutes
    selected_sort = "min-missing-ingredients" # min-missing-ingredients
    selected_number = 1 # Number of desired results
    selected_fillIngredients = True

    data = retrieve_recipes_by_ingredients(selected_search_criteria,selected_cuisine,selected_diet,selected_intolerances,selected_dish_type,selected_maxReadyTime,selected_sort,selected_number,selected_fillIngredients)
    print(data)