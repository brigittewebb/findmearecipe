# this is the app/spoonacular_service.py file...

import os

from dotenv import load_dotenv


load_dotenv() # looks in the ".env" file for env vars

API_KEY = os.getenv("SPOONACULAR_API_KEY", default="demo")