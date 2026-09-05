"""Task 2: Add, update, and display student grades using a dictionary."""


students = {
    "Rahul": 85,
    "Amit": 78,
    "Neha": 92
}


# -  To Add a new student----------------------------

print("Initial student grades:", students)

name = input("Enter student name to ADD: ").strip().title()


try:

    grade = int(input("Enter new grade (0-100): "))
        
    if 0 <= grade <= 100:
            students[name] = grade
            print(f"Grade for {name} updated successfully.")
            print("Final updated dictionary is :", students)
    else:
        print("Grade must be between 0 and 100.")

except ValueError:
    print("Invalid input! Please enter a numeric grade.")

