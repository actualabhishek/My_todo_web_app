import streamlit as st
import main_function

todos = main_function.read_file()


def add_todo():
    add_todo = st.session_state["new_todo"] + '\n'
    todos.append(add_todo)
    main_function.write_file(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        main_function.write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input("Enter Todo", placeholder="add todo...", key="new_todo", on_change=add_todo)

# st.session_state
