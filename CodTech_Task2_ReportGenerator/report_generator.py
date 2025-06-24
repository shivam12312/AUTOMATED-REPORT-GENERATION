import pandas as pd
from fpdf import FPDF

# Load the CSV data
data = pd.read_csv("data.csv")

# Basic analysis
average_marks = data['Marks'].mean()
highest = data.loc[data['Marks'].idxmax()]
lowest = data.loc[data['Marks'].idxmin()]

# Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Student Performance Report", ln=True, align='C')
pdf.ln(10)

# Summary
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(200, 10, f"Top Scorer: {highest['Name']} ({highest['Marks']})", ln=True)
pdf.cell(200, 10, f"Lowest Scorer: {lowest['Name']} ({lowest['Marks']})", ln=True)
pdf.ln(10)

# Table header
pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, "Name", 1)
pdf.cell(60, 10, "Department", 1)
pdf.cell(60, 10, "Marks", 1)
pdf.ln()

# Table rows
pdf.set_font("Arial", size=12)
for index, row in data.iterrows():
    pdf.cell(60, 10, row["Name"], 1)
    pdf.cell(60, 10, row["Department"], 1)
    pdf.cell(60, 10, str(row["Marks"]), 1)
    pdf.ln()

# Save PDF
pdf.output("student_report.pdf")
print("✅ Report generated: student_report.pdf")
