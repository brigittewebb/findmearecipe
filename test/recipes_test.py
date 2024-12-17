# this is the "test/recipes_test.py" file...

from app.recipes import retrieve_recipes_by_ingredients, retrieve_recipes_by_keyword, retrieve_recipe_info

def test_data_fetching_by_ingredients():
    
    selected_search_criteria = ["apples","flour","sugar"]
    selected_cuisine = None # Type of food (ex., "Italian")--dropdown list
    selected_diet = None # Special diets (ex., "vegetarian")--dropdown list
    selected_intolerances = None # Dietary resrictions (ex., "gluten")--dropdown list
    selected_dish_type = None # Type of dish (ex., "main course")--dropdown list
    selected_maxReadyTime = None # Denoted in minutes
    selected_sort = "min-missing-ingredients" # min-missing-ingredients
    selected_number = 1 # Number of desired results
    selected_fillIngredients = True
    
    data = retrieve_recipes_by_ingredients(selected_search_criteria,selected_cuisine, selected_diet, selected_intolerances, selected_dish_type, selected_maxReadyTime, selected_sort, selected_number, selected_fillIngredients)
    assert isinstance(data, list)
    assert len(data) == selected_number

def test_data_fetching_by_keyword():
    
    selected_search_criteria = "banana bread"
    selected_diet = None # Special diets (ex., "vegetarian")--dropdown list
    selected_intolerances = None # Dietary resrictions (ex., "gluten")--dropdown list
    selected_number = 1 # Number of desired results
    selected_fillIngredients = True
    
    data = retrieve_recipes_by_keyword(selected_search_criteria, selected_diet, selected_intolerances, selected_number, selected_fillIngredients)
    assert isinstance(data, list)
    assert len(data) == selected_number

def test_data_fetching_by_recipe_id():

    recipe_id = 646541

    data = retrieve_recipe_info(recipe_id)
    assert isinstance(data, dict)
    assert data["title"] == "Heart Healthy, Whole-Grain Brownies"