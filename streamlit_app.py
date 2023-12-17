import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd

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

# Initialize session state for participation data
if 'participation_data' not in st.session_state:
    st.session_state.participation_data = pd.DataFrame(columns=["Employee ID", "Project ID", "Participation"])

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
        AgGrid(employees)

    elif section == "Project Information":
        st.header("Project Information")
        AgGrid(projects)

    elif section == "Assign Participation":
        st.header("Assign Participation")
        grid_options = GridOptionsBuilder.from_dataframe(st.session_state.participation_data)
        grid_options.configure_column("Employee ID", editable=True, cellEditor='agSelectCellEditor', cellEditorParams={
            'values': employees['id'].tolist()})
        grid_options.configure_column("Project ID", editable=True, cellEditor='agSelectCellEditor', cellEditorParams={
            'values': projects['id'].tolist()})
        grid_options.configure_column("Participation", editable=True, type=["numericColumn", "numberColumnFilter", "customNumericFormat"], precision=2)

        grid_options.enable_pagination()
        grid_options.set_pagination_auto_size(True)
        grid_response = AgGrid(
            st.session_state.participation_data, 
            gridOptions=grid_options.build(), 
            fit_columns_on_grid_load=True,
            update_mode='MODEL_CHANGED',
            enable_enterprise_modules=True,
            height=300,
            reload_data=False
        )

        st.session_state.participation_data = grid_response['data']

if __name__ == "__main__":
    main()
