
# this is the "web_app/routes/recipes_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.recipes import retrieve_recipes, retrieve_recipe_info

recipes_routes = Blueprint("recipes_routes", __name__)

@recipes_routes.route("/")
def Home():
    print("HOME...")
    return render_template("home.html")

#
# RECIPES BY INGREDIENTS ROUTES
#

@recipes_routes.route("/recipes/by_ingredients/form")
def recipes_form():
    print("RECIPES FORM...")
    return render_template("recipes_form_by_ingredients.html")

#@recipes_routes.route("/recipes/by_ingredients/list", methods=["POST"])
@recipes_routes.route("/recipes/by_ingredients/list", methods=["GET", "POST"])
def recipes_list():
    print("RECIPES LIST...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    # Grabbing some data from the dictionary sent by the form (or URL parameters)
    search_criteria = request_data.get("search_criteria")
    cuisine = request_data.get("cuisine")
    diet = request_data.get("diet")
    intolerances = request_data.get("intolerances")
    dish_type = request_data.get("dish_type")
    maxReadyTime = request_data.get("MaxReadyTime")
    sort = "min-missing-ingredients"
    number = request_data.get("number")
    fillIngredients= True

    try:
        data = retrieve_recipes(search_criteria=search_criteria,cuisine=cuisine,diet=diet,intolerances=intolerances,dish_type=dish_type,maxReadyTime=maxReadyTime,sort=sort,number=number,fillIngredients=fillIngredients)

        flash("Fetched Recipe Data!", "success") # First parameter is message to display, second parameter is bootstrap color code
        return render_template("recipes_list_by_ingredients.html",
            data=data,
        )
    except Exception as err:
        print('OOPS', err)

        flash("Recipe Data Error. Please check your inputs and try again!", "danger")
        return redirect("/recipes/by_ingredients/form")
    
@recipes_routes.route("/recipe/by_ingredients/info", methods=["POST"])
def recipe_info():
    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    # Grabbing some data from the dictionary sent by the form (or URL parameters)
    recipe_id = request_data["recipe_id"]
    missing_ingredients = request_data["missing_ingredients"]
    parsed_missing_ingredients = eval(missing_ingredients)
    
    try:
        recipe = retrieve_recipe_info(recipe_id=recipe_id)
        flash("Fetched Recipe Data!", "success") # First parameter is message to display, second parameter is bootstrap color code
        return render_template("recipe_info_by_ingredients.html",
            recipe=recipe,
            missing_ingredients=parsed_missing_ingredients
        )
    except Exception as err:
        print('OOPS', err)

        flash("Recipe Data Error. Please check your inputs and try again!", "danger")
        return redirect("/recipes/by_ingredients/form")


#
# API ROUTES
#

@recipes_routes.route("/api/recipes")
def recipes_api():
    print("RECIPES DATA (API)...")

    # for data supplied via GET request, url params are in request.args:
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    search_criteria = url_params.get("search_criteria")
    cuisine = url_params.get("cuisine")
    diet = url_params.get("diet")
    intolerances = url_params.get("intolerances")
    dish_type = url_params.get("dish_type")
    maxReadyTime = url_params.get("maxReadyTime")
    sort = "min-missing-ingredients"
    number = url_params.get("number")
    fillIngredients= True

    try:
        data = retrieve_recipes(search_criteria=search_criteria,cuisine=cuisine,diet=diet,intolerances=intolerances,dish_type=dish_type,maxReadyTime=maxReadyTime,sort=sort,number=number,fillIngredients=fillIngredients)
        return {"data": data }
    except Exception as err:
        print('OOPS', err)
        return {"message":"Recipe Data Error. Please try again."}, 404