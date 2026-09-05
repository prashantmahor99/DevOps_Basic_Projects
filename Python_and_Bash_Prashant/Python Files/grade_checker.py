"""Task 1: Display a grade according to the score entered by the user."""

try:
    score = int(input("Enter your score: "))

    for i in range(1):
        if score < 0 or score > 100:
            print("Please enter a score between 0 and 100.")
        elif score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        print(f"Your Grade is: {grade}")

except ValueError:
    print("Invalid input. Please enter a number.")