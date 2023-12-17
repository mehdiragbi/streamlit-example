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

        # Participation Input Form
        with st.form("participation_form"):
            for i in range(len(st.session_state.participation_data) + 1):
                cols = st.columns([3, 3, 2])
                with cols[0]:
                    employee_choice = st.selectbox("Select Employee", [""] + list(employees['id']), key=f"emp_{i}")
                with cols[1]:
                    project_choice = st.selectbox("Select Project", [""] + list(projects['id']), key=f"proj_{i}")
                with cols[2]:
                    participation = st.number_input("Participation Percentage", min_value=0, max_value=100, format="%d%%", key=f"part_{i}")
                
                # Add row to participation data
                if employee_choice and project_choice and participation:
                    st.session_state.participation_data.loc[i] = [employee_choice, project_choice, participation]

            submit = st.form_submit_button("Submit")

        if submit:
            st.success("Participation Data Updated")

        st.subheader("Current Participation Mapping")
        st.dataframe(st.session_state.participation_data)

if __name__ == "__main__":
    main()
