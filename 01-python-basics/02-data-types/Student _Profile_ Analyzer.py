
# Project: Student Profile Analyzer

print("🎓 STUDENT PROFILE ANALYZER")
print("===========================")

# Basic Data Types

name = "Ruchita"              # String
age = 25                      # Integer
percentage = 85.5             # Float
complex_number = 3 + 4j       # Complex
is_student = True             # Boolean
future_job = None             # NoneType


# Collection Data Types

skills = ["Python", "SQL", "Excel"]       # List
location = (18.52, 73.85)                 # Tuple
unique_skills = {"Python", "SQL", "Excel"} # Set

student = {                               # Dictionary
    "name": name,
    "age": age,
    "percentage": percentage
}


# Display Student Information

print("\n📋 STUDENT INFORMATION")
print("----------------------")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Percentage: {percentage}%")
print(f"Student: {is_student}")
print(f"Skills: {skills}")
print(f"Location: {location}")
print(f"Unique Skills: {unique_skills}")
print(f"Student Details: {student}")
print(f"Future Job: {future_job}")


# Checking Data Types

print("\n🔍 DATA TYPES")
print("-------------")

print("Name:", type(name))
print("Age:", type(age))
print("Percentage:", type(percentage))
print("Complex Number:", type(complex_number))
print("Student:", type(is_student))
print("Skills:", type(skills))
print("Location:", type(location))
print("Unique Skills:", type(unique_skills))
print("Student Details:", type(student))
print("Future Job:", type(future_job))