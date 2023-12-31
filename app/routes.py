from flask import render_template, send_from_directory, request
import bcrypt
from app import app
from app.models import User, Category, Space
from app.middleware import auth
from app.database import session
from app.service import get_component_by_id, update_component, get_category_by_id, get_space_by_id, get_all_categories, get_all_spaces
from datetime import datetime

# Host static files


@app.route("/static/<path:path>")
def send_assets(path):
    return send_from_directory('app/static', path)

# Upload Image


@app.post("/api/upload")
def upload_image():
    print(request.files)
    file = request.files["file"]
    file.save(f"app/static/images/{file.filename}")
    return {"file": file.filename}, 200

# Edit component form


@app.get("/admin/component/edit/<int:id>")
def edit_component(id):
    component = get_component_by_id(id)
    category = get_category_by_id(component.category_id)
    space = get_space_by_id(component.space_id)
    categories = get_all_categories()
    spaces = get_all_spaces()
    return render_template("edit_component.html", component=component, space=space, category=category, categories=categories, spaces=spaces)


# Api call to edit component
@app.put("/api/admin/component/<int:id>")
def api_edit_component(id):
    component = get_component_by_id(id)
    component_body = request.json

    component.title = component_body["title"]
    component.image = component_body["image"]
    component.description = component_body["description"]
    # component.image = component_body["image"]
    component.category_id = component_body["category_id"]
    component.space_id = component_body["space_id"]
    component.purchase_date = datetime.strptime(
        component_body["purchase_date"], "%Y-%m-%d")
    component.termination_date = datetime.strptime(
        component_body["termination_date"], "%Y-%m-%d")
    component.status = component_body["status"]

    update_component(component)

    return "updated component", 200


@app.get("/admin/category/create")
def add_category():
    return render_template("add_category.html")


@app.post("/api/admin/category")
def api_add_category():
    body = request.json
    category = Category(name=body["name"])
    session.add(category)
    session.commit()
    return "added category", 200


@app.get("/admin/space/create")
def add_space():
    return render_template("add_space.html")


@app.post("/api/admin/space")
def api_add_space():
    body = request.json
    space = Space(name=body["name"])
    session.add(space)
    session.commit()
    return "added space", 200
