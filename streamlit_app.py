import streamlit as st
from pyecharts.charts import Bar
from pyecharts import options as opts
from streamlit_echarts import st_pyecharts

# Fake employee data
def load_employee_data():
    return [
        {"id": "1", "name": "Alice", "role": "Developer"},
        {"id": "2", "name": "Bob", "role": "Designer"},
        # Add more fake employees as needed
    ]

# Fake project data
def load_project_data():
    return [
        {"id": "P1", "name": "Project Alpha"},
        {"id": "P2", "name": "Project Beta"},
        # Add more fake projects as needed
    ]

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

    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the section",
                                    ["Employee Information", "Project Information", "Participation Input"])

    if app_mode == "Employee Information":
        st.subheader("Employee Information")
        employees = load_employee_data()
        st.write(employees)

    elif app_mode == "Project Information":
        st.subheader("Project Information")
        projects = load_project_data()
        st.write(projects)

    elif app_mode == "Participation Input":
        st.subheader("Assign Participation")
        employee_id = st.selectbox("Select Employee", [e['id'] for e in load_employee_data()])
        project_id = st.selectbox("Select Project", [p['id'] for p in load_project_data()])
        participation = st.slider("Participation Percentage", 0, 100)
        
        submit = st.button("Submit")
        if submit:
            st.success("Participation Updated")
            sample_data = [{"name": "Alice", "participation": participation}]
            chart = generate_chart(sample_data)
            st_pyecharts(chart)

if __name__ == "__main__":
    main()
