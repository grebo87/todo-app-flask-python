"""Defines all the functions related to the database"""
from app import db

def fetch_all() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from tasks;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "name": result[1],
            "status": result[2]
        }
        todo_list.append(item)

    return todo_list

def fetch_by_id(task_id: int) -> dict:
    conn = db.connect()
    query = 'Select * from tasks where id="{}";'.format(task_id)
    query_results = conn.execute(query)
    conn.close()

    return query_results.fetchone()

def update(task_id: int, text: str) -> None:
    conn = db.connect()
    query = 'Update tasks set name = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()

def delete(task_id) -> None:
    conn = db.connect()
    query = 'Delete From tasks where id={};'.format(task_id)
    conn.execute(query)
    conn.close()

def insert_new_task(text: str) ->  int:
    conn = db.connect()
    query = 'Insert Into tasks (name, status) VALUES ("{}", "{}");'.format(
        text, "Todo")
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id

def update_status_task(task_id: int, status: str) -> None:
    conn = db.connect()
    query = 'Update tasks set status = "{}" where id = {};'.format(status, task_id)
    conn.execute(query)
    conn.close()