import streamlit as st
from pyecharts.charts import Bar
from pyecharts import options as opts
from streamlit_echarts import st_pyecharts

# Fake employee data
employees = [
    {"id": "1", "name": "Alice", "role": "Developer"},
    {"id": "2", "name": "Bob", "role": "Designer"},
    # Add more fake employees as needed
]

# Fake project data
projects = [
    {"id": "P1", "name": "Project Alpha"},
    {"id": "P2", "name": "Project Beta"},
    # Add more fake projects as needed
]

# Participation mapping data
participation_data = []

# Function to generate a bar chart using Echarts
def generate_chart(data):
    bar = Bar(init_opts=opts.InitOpts(width="700px", height="400px"))
    bar.add_xaxis([d['name'] for d in data])
    bar.add_yaxis("Participation", [d['participation'] for d in data])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Employee Participation"))
    return bar

# Streamlit app layout
def main():
    st.title("Corporate Data Input App")

    # Employee Information Section
    st.header("Employee Information")
    for employee in employees:
        cols = st.columns([1, 2, 2])
        with cols[0]:
            employee['id'] = st.text_input("ID", employee['id'])
        with cols[1]:
            employee['name'] = st.text_input("Name", employee['name'])
        with cols[2]:
            employee['role'] = st.text_input("Role", employee['role'])

    # Project Information Section
    st.header("Project Information")
    for project in projects:
        cols = st.columns([1, 3])
        with cols[0]:
            project['id'] = st.text_input("Project ID", project['id'])
        with cols[1]:
            project['name'] = st.text_input("Project Name", project['name'])

    # Participation Input Section
    st.header("Assign Participation")
    with st.form("participation_form"):
        employee_id = st.selectbox("Select Employee", [e['id'] for e in employees])
        project_id = st.selectbox("Select Project", [p['id'] for p in projects])
        participation = st.slider("Participation Percentage", 0, 100)
        submit = st.form_submit_button("Submit")

    if submit:
        participation_data.append({"employee_id": employee_id, "project_id": project_id, "participation": participation})
        st.success("Participation Updated")

        # Display participation data
        st.subheader("Current Participation Mapping")
        for data in participation_data:
            cols = st.columns([1, 1, 1])
            with cols[0]:
                st.text_input("Employee ID", data['employee_id'], key=f"emp_{data['employee_id']}")
            with cols[1]:
                st.text_input("Project ID", data['project_id'], key=f"proj_{data['project_id']}")
            with cols[2]:
                st.text_input("Participation", str(data['participation']), key=f"part_{data['participation']}")

        # Example chart (Replace with actual data)
        chart = generate_chart(participation_data)
        st_pyecharts(chart)

if __name__ == "__main__":
    main()
