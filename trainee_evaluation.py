# Python program: Trainee Evaluation with Error Checking

# Function to safely get a score between 0 and 100
def get_score(subject):
    while True:
        try:
            score = float(input(f"Enter trainee score in {subject} (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100. Try again.")
        except ValueError:
            print("Error: Please enter a valid number.")

# Capture trainee's full name
trainee_name = input("Enter trainee full name: ")

# Capture scores with error checking
python_syntax = get_score("Python Syntax")
problem_solving = get_score("Problem Solving")
mini_project = get_score("Mini Project")

# Calculate total and average
total_score = python_syntax + problem_solving + mini_project
average_score = total_score / 3

# Assign performance grade
if average_score >= 80:
    grade = "Excellent"
elif 70 <= average_score <= 79:
    grade = "Very Good"
elif 60 <= average_score <= 69:
    grade = "Good"
elif 50 <= average_score <= 59:
    grade = "Fair"
else:
    grade = "Needs Improvement"

# Determine completion status
status = "Competent" if average_score >= 50 else "Not Yet Competent"

# Display professional report
print("\n========== Trainee Performance Report ==========")
print(f"Trainee Name        : {trainee_name}")
print(f"Python Syntax Score : {python_syntax}")
print(f"Problem Solving     : {problem_solving}")
print(f"Mini Project Score  : {mini_project}")
print(f"Total Score         : {total_score}")
print(f"Average Score       : {average_score:.2f}")
print(f"Performance Grade   : {grade}")
print(f"Completion Status   : {status}")
print("===============================================")