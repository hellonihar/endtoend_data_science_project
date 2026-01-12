import pandas as pd
import random

# Define possible values for each categorical column
genders = ["Male", "Female"]
ethnicities = ["Group A", "Group B", "Group C", "Group D", "Group E"]
lunch_types = ["Standard", "Free/Reduced"]
test_prep_status = ["Completed", "None"]

# Function to generate random scores between 0 and 100
def random_score():
    return random.randint(40, 100)  # keeping scores realistic

# Number of sample students
num_students = 500

# Generate the dataset
data = []
for _ in range(num_students):
    gender = random.choice(genders)
    ethnicity = random.choice(ethnicities)
    lunch = random.choice(lunch_types)
    test_prep = random.choice(test_prep_status)
    math_score = random_score()
    reading_score = random_score()
    writing_score = random_score()
    
    data.append([gender, ethnicity, lunch, test_prep, math_score, reading_score, writing_score])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Gender", "Ethnicity", "Lunch", "Test Preparation Status",
    "Math Score", "Reading Score", "Writing Score"
])

# Save to Excel
output_file = "student_sample_data.xlsx"
df.to_excel(output_file, index=False)

print(f"Sample student dataset saved as '{output_file}'")