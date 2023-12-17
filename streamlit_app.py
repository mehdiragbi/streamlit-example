import streamlit as st
import pandas as pd

# Initialize session state for participation data
if 'participation_data' not in st.session_state:
    st.session_state.participation_data = pd.DataFrame(columns=["Employee ID", "Project ID", "Participation"])

# Sample data for employees and projects
employees = pd.DataFrame([
    {"id": "1", "name": "Alice", "role": "Developer"},
    {"id": "2", "name": "Bob", "role": "Designer"},
    # ... more employees
])

projects = pd.DataFrame([
    {"id": "P1", "name": "Project Alpha"},
    {"id": "P2", "name": "Project Beta"},
    # ... more projects
])

# Streamlit app layout
def main():
    st.title("Corporate Data Input App")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    section = st.sidebar.radio("Go to", ["Home", "Employee Information", "Project Information", "Assign Participation"])

    if section == "Home":
        st.header("Welcome to the Corporate Data Input App")
        st.write("Select a section from the sidebar to begin.")

    elif section == "Employee Information":
        st.header("Employee Information")
        st.dataframe(employees)

    elif section == "Project Information":
        st.header("Project Information")
        st.dataframe(projects)

    elif section == "Assign Participation":
        st.header("Assign Participation")
        with st.form("participation_form"):
            employee_choice = st.selectbox("Select Employee", [""] + list(employees['id']))
            project_choice = st.selectbox("Select Project", [""] + list(projects['id']))
            participation = st.number_input("Participation Percentage", min_value=0, max_value=100, format="%d%%")
            submit = st.form_submit_button("Submit")

        if submit and employee_choice and project_choice and participation is not None:
            new_row = {"Employee ID": employee_choice, "Project ID": project_choice, "Participation": participation}
            st.session_state.participation_data = st.session_state.participation_data.append(new_row, ignore_index=True)
            st.success("Participation Data Updated")

        st.subheader("Current Participation Mapping")
        st.dataframe(st.session_state.participation_data)

if __name__ == "__main__":
    main()
