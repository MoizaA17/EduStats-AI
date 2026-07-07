import streamlit as st
import numpy as np

# Setting the page configuration
st.title("🎓 EduStats AI")
st.write("Welcome to EduStats AI! This application provides insights and analytics for educational data. Explore various features and visualize your data effectively.")

user_input = st.text_input("Enter students marks seperated by commas:")
submit_btn = st.button("Submit")


if submit_btn:
    if user_input:
        st.success("Data submitted successfully!")
        st.divider()

        # Splitting user input into marks
        marks = user_input.split(",")

        # Converting marks to integers
        students_marks = [int(mark) for mark in marks]

        # Converting the list of marks to a NumPy array for further analysis
        students_marks = np.array(students_marks)

        # Calculating statistics
        st.subheader("📊 Summary")

        #colums = 3
        col1, col2, col3 = st.columns(3)
        #Average
        average = students_marks.mean()
        col1.markdown("#### Average: ####")
        col1.metric(label = " ", value=average.round(2)) 
        
        #highest
        highest = students_marks.max()
        col2.markdown("#### Highest Marks: #### ")
        col2.metric(label = " " , value=highest)

        #lowest
        lowest = students_marks.min()
        col3.markdown("#### Lowest Marks: ####")
        col3.metric(label = " " ,value=lowest)
        st.divider()

        #Topper
        st.subheader("🏆 Top Performer")
        topper_index = students_marks.argmax()
        st.metric(label = "Student: #" , value = topper_index + 1)
        st.metric(label = "Marks: ",value = students_marks[topper_index])
        st.divider()

        #Passed Students
        st.subheader("✅ Passed Students")
        passed_students = students_marks[students_marks>=50]
        st.metric(label="Passed Students Count", value=len(passed_students))
        st.divider()

        #Failed Students
        st.subheader("❌ Failed Students")
        failed_students = students_marks[students_marks<50]
        st.metric(label="Failed Students Count", value=len(failed_students))
        st.divider()

        #Passed Students Percentage
        st.subheader("🎉 Passed Students Percentage")
        pass_percentage = (len(passed_students)/len(students_marks)) * 100
        st.metric(label= "Percentage of Passed Students: ", value = round(pass_percentage, 2))
        st.divider()

        st.space("large")

        st.markdown("<p style= 'text-align: center;'> Developed by Moizah Kafayat | Powered by Streamlit and NumPy </p>", unsafe_allow_html=True)
    else:
        st.error("Please enter the marks to analyze.")

