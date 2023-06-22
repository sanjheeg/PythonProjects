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

# creates checkboxes for all todos, removes if marked done
for index, todo in enumerate(todos):
	checkbox = sl.checkbox(todo, key=todo)
	if checkbox:
		todos.pop(index)
		write_todos(todos)
		del sl.session_state[todo]
		# used for checkboxes, will rerun the code, removing above todo
		sl.experimental_rerun()


sl.text_input(label="", placeholder="add a new todo", on_change=add_todo, key="new")
