from flask import render_template, send_from_directory
import bcrypt
from app import app
from app.models import User
from app.middleware import auth

# Host static files
@app.route("/static/<path:path>")
def send_assets(path):
    return send_from_directory('app/static', path)
