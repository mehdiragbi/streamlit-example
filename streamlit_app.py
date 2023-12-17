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

# Apply custom styles
def apply_custom_styles():
    st.markdown(f"""
        <style>
            /* Main page background */
            body {{
                background-color: #ffffff;
            }}
            /* Primary button color */
            .stButton>button {{
                border: 2px solid #cccccc;
                background-color: #ff4b4b;
                color: #ffffff;
            }}
            /* Widget background */
            .stTextInput, .stSelectbox, .stSlider {{
                background-color: #cccccc;
            }}
            /* Text color */
            .reportview-container .markdown-text, .reportview-container .streamlit-expanderHeader {{
                color: #333333;
            }}
            /* Headers color */
            h1, h2, h3, h4, h5, h6 {{
                color: #ff4b4b;
            }}
            /* Dataframe styling */
            .stDataFrame {{
                background-color: #ffffff;
            }}
            /* Modify other Streamlit component styles here */
        </style>
    """, unsafe_allow_html=True)

# Streamlit app layout
def main():
    # Inject custom CSS for styling
    apply_custom_styles()

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
