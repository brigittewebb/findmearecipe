# this is the "test/recipes_test.py" file...

from app.recipes import retrieve_recipes

def test_data_fetching():
    
    selected_query = ["apples","flour","sugar"]
    selected_cuisine = None # Type of food (ex., "Italian")--dropdown list
    selected_diet = None # Special diets (ex., "vegetarian")--dropdown list
    selected_intolerances = None # Dietary resrictions (ex., "gluten")--dropdown list
    selected_dish_type = None # Type of dish (ex., "main course")--dropdown list
    selected_maxReadyTime = None # Denoted in minutes
    selected_sort = "min-missing-ingredients" # min-missing-ingredients
    selected_number = 1 # Number of desired results
    selected_fillIngredients = True
    
    data = retrieve_recipes(selected_query,selected_cuisine, selected_diet, selected_intolerances, selected_dish_type, selected_maxReadyTime, selected_sort, selected_number, selected_fillIngredients)
    assert isinstance(data, list)
    assert len(data) == selected_number