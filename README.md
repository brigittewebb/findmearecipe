# findmearecipe
Find recipe ideas based on filters such as ingredients you already have in your kitchen, cuisine type, and dietary preferences.

## Setup

Create and activate a virtual environment (first time only):

```sh
conda create -n findmearecipe-env python=3.13
```

Activate the environment (whenever you come back to this project):

```sh
conda activate findmearecipe-env
```

Install packages:

```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://spoonacular.com/food-api) from Spoonacular.

Create a ".env" file and add contents like the following (using your own Spoonacular API Key):

```sh
# this is the ".env" file:
SPOONACULAR_API_KEY="..."
```

## Usage

Run the receipe file to pull data from the API:

```sh
python -m app.recipes
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:

```sh
pytest
```