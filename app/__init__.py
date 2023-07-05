from flask import Flask

# Create an instance of the Flask application
app = Flask(__name__)

# Importing routes and models
from app import routes, models, database, service, middleware