from flask import render_template, send_from_directory

from app import app


# Host static files
@app.route("/static/<path:path>")
def send_assets(path):
    return send_from_directory('app/static', path)
