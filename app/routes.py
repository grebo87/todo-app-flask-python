from sqlalchemy.util.langhelpers import methods_equivalent
from app import app
from flask import render_template, request, jsonify
from app import database as db_helper

@app.route("/")
def homepage():
    tasks = db_helper.fetch_all()
    return render_template('index.html', tasks=tasks)

@app.route("/tasks",methods=['POST'])
def cerate_task():
    data = request.get_json()
    task_id = db_helper.insert_new_task(data["description"])
    response = { "success": True, "data": (task_id) }
    return jsonify(response)

@app.route("/tasks/<int:task_id>", methods=['GET'])
def show_task(task_id):
    task = db_helper.fetch_by_id(task_id)
    response = { "success": True, "data": dict(task) }
    return jsonify(response)

# @app.route("/tasks/<int:task_id>/edit", methods=['GET'])
# def edit_task(task_id):
#     task = db_helper.fetch_by_id(task_id)
#     response = { "success": True, "data": dict(task) }
#     return jsonify(response)

@app.route("/tasks/<int:task_id>", methods= ['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = db_helper.update(task_id, data['description'])
    response = { "success": True, "data": task }
    return jsonify(response)

@app.route("/tasks/<int:task_id>", methods= ['DELETE'])
def delete_task(task_id):
    task = db_helper.delete(task_id)
    response = { "success": True, "data": task }
    return jsonify(response)

@app.route("/tasks/<int:task_id>/change_status", methods = ['POST'])
def change_status(task_id):
    data = request.get_json()
    task = db_helper.update_status_task(task_id,data['status'])
    response = { "success": True, "data": task }
    return jsonify(response)