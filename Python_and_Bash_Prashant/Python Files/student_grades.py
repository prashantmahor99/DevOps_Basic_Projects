students = {
    "Rahul": 85,
    "Amit": 78,
    "Neha": 92
}

print("Initial student grades:", students)

# Add a new student and grade
students["Prashant"] = 88
print("After adding Prashant:", students)

# Update an existing student's grade
students["Amit"] = 82
print("After updating Amit's grade:", students)

# Print all student grades
print("\nAll Student Grades:")
for name, grade in students.items():
    print(name, ":", grade)

# Basic if/else operation with dictionary
student_name = "Prashant"
if student_name in students:
    print(f"\n{student_name}'s grade is: {students[student_name]}")
else:
    print("Student not found")
