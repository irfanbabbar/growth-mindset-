import streamlit as st

# App title
st.title('To-Do List App')

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Sidebar for task management
st.sidebar.header('Manage Tasks')

# Function to add a new task
def add_task(new_task):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.success("Task added successfully!")
    else:
        st.warning("Task cannot be empty!")

# Function to update a task
def update_task(index, new_task):
    if new_task.strip():
        st.session_state.tasks[index]["task"] = new_task
        st.success("Task updated successfully!")
    else:
        st.warning("Task cannot be empty!")

# Function to delete a task
def delete_task(index):
    del st.session_state.tasks[index]
    st.success("Task deleted successfully!")

# Function to clear all tasks
def clear_all_tasks():
    st.session_state.tasks = []
    st.success("All tasks cleared successfully!")

# Input field for new task
new_task = st.sidebar.text_input('Enter new task:', placeholder="Enter task here...")

# Add task button
if st.sidebar.button("Add Task"):
    add_task(new_task)

# Display tasks
st.subheader("Your To-Do List")
if not st.session_state.tasks:
    st.info("No tasks added yet. Start by adding a task from the sidebar.")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7,0.10,0.15])
        
        # Mark task as completed
        completed = col1.checkbox(f"**{task['task']}**", task["completed"], key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed
        
        # Edit task
        if col3.button("✏️", key=f"edit_{index}"):
            st.session_state.edit_index = index  # Store the index of the task being edited
        
        # If editing, show the text input and save button
        if "edit_index" in st.session_state and st.session_state.edit_index == index:
            new_task = st.text_input("Edit task", task["task"], key=f"edit_input_{index}")
            if st.button("Save", key=f"save_{index}"):
                update_task(index, new_task)
                del st.session_state.edit_index  # Clear the edit state
                st.rerun()  
        
        # Delete task
        if col3.button("🗑️", key=f"delete_{index}"):
            delete_task(index)
            st.rerun()  

# Clear all tasks button
if st.sidebar.button("Clear All Tasks"):
    clear_all_tasks()

# Footer
st.markdown("---")
st.caption("This is a To-Do List test app. Enjoy!")