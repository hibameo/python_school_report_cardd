import streamlit as st
from fpdf import FPDF

# School name
school_name = "Al Hamd Cadet Schooling System"

# List of subjects
subjects = ["English", "Urdu", "Math", "Islamiat", "Science", "Social Studies", "Computer", "Arts", "Sindhi", "General Knowledge (GK)"]

# Function to determine grade based on marks
def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Function to generate PDF
def generate_pdf(student_name, roll_number, student_class, marks, grades):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt=school_name, ln=True, align='C')
    
    # Student details
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, txt=f"Student Name: {student_name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Roll Number: {roll_number}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Class: {student_class}", ln=True, align='L')  # Add Class

    # Subjects, marks, and grades
    pdf.ln(10)  # Line break
    pdf.cell(100, 10, 'Subject', 1, 0, 'C')
    pdf.cell(50, 10, 'Marks', 1, 0, 'C')
    pdf.cell(40, 10, 'Grade', 1, 1, 'C')

    for i, subject in enumerate(subjects):
        pdf.cell(100, 10, subject, 1, 0, 'C')
        pdf.cell(50, 10, str(marks[i]), 1, 0, 'C')
        pdf.cell(40, 10, grades[i], 1, 1, 'C')

    # Teacher's and Principal's signature
    pdf.ln(15)  # Line break before signatures
    pdf.set_font('Arial', 'I', 12)
    pdf.cell(95, 10, 'Teacher\'s Signature: __________________', 0, 0, 'L')
    pdf.cell(95, 10, 'Principal\'s Signature: __________________', 0, 1, 'L')

    # Save PDF
    pdf.output(f"{student_name}_Report_Card.pdf")

# Streamlit UI
def main():
    st.title("Digital Student Report Card System")
    
    # School Name
    st.header(school_name)
    
    # Input student details
    roll_number = st.text_input("Enter Student's Roll Number:")
    student_name = st.text_input("Enter Student's Name:")
    student_class = st.text_input("Enter Student's Class:")  # New input for Class
    
    # Input marks for each subject
    marks = []
    grades = []
    for subject in subjects:
        mark = st.number_input(f"Enter marks for {subject}:", min_value=0, max_value=100)
        marks.append(mark)
        grades.append(get_grade(mark))
    
    # Button to generate report card
    if st.button("Generate Report Card"):
        if student_name and roll_number and student_class:
            generate_pdf(student_name, roll_number, student_class, marks, grades)
            st.success(f"Report Card for {student_name} has been generated.")
            st.download_button(
                label="Download PDF",
                data=open(f"{student_name}_Report_Card.pdf", "rb").read(),
                file_name=f"{student_name}_Report_Card.pdf",
                mime="application/pdf"
            )
        else:
            st.error("Please enter all the student's details (Name, Roll Number, and Class).")

if __name__ == "__main__":
    main()
