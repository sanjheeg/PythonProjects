import streamlit as sl

def get_todos(filepath):
	with open(filepath, "r") as file:
		todos = file.readlines()
	return todos

def write_todos(todo_list, filepath = "/Users/sanjheegupta/PycharmProjects/PythonCourse/web_todo_app/todo_data"):
	with open(filepath, "w") as file:
		file.writelines(todo_list)

todos = get_todos("/Users/sanjheegupta/PycharmProjects/PythonCourse/web_todo_app/todo_data")


def add_todo():
	todo = sl.session_state["new"]
	todos.append(todo + "\n")
	write_todos(todos)

sl.title("My Todo App")
sl.subheader("will help you increase your productivity")

for todo in todos:
	sl.checkbox(todo)


sl.text_input(label="", placeholder="add a new todo", on_change=add_todo, key="new")
