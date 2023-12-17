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

    # Employee Information Section
    st.header("Employee Information")
    st.dataframe(employees)

    # Project Information Section
    st.header("Project Information")
    st.dataframe(projects)

    # Participation Input Section
    st.header("Assign Participation")
    with st.form("participation_form"):
        employee_id = st.selectbox("Select Employee", employees['id'])
        project_id = st.selectbox("Select Project", projects['id'])
        participation = st.slider("Participation Percentage", 0, 100, 50)
        submit = st.form_submit_button("Submit")

    if submit:
        # Add the new mapping to the participation_data DataFrame in session state
        new_row = {"Employee ID": employee_id, "Project ID": project_id, "Participation": participation}
        st.session_state.participation_data = st.session_state.participation_data.append(new_row, ignore_index=True)
        st.success("Participation Updated")

    # Display participation data
    st.subheader("Current Participation Mapping")
    st.dataframe(st.session_state.participation_data)

if __name__ == "__main__":
    main()
