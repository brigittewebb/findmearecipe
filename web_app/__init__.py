# this is the "web_app/__init__.py" file...

# This code allows you to import routes from other files within the directory

import os
from flask import Flask

from web_app.routes.recipes_routes import recipes_routes # Need to do this for each routes file

SECRET_KEY = os.getenv("SECRET_KEY", default="dkjwleijowijlksdaqwanbbdskne")

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.register_blueprint(recipes_routes) # Need to do this for each routes file
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)