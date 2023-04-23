print("Welcome to the Job Portal\n")

# Define job vacancies
job_vacancies = {
    "1": "Software Engineer",
    "2": "Data Analyst",
    "3": "Web Developer",
    "4": "UI/UX Designer"
}

# Display job vacancies
print("Available Job Vacancies:")
for key, value in job_vacancies.items():
    print(key + ". " + value)

# Get user input
first_name = input("\nEnter First Name: ")
last_name = input("Enter Last Name: ")
email = input("Enter Email: ")
contact = input("Enter Contact Details: ")
marital_status = input("Enter Marital Status: ")
education = input("Enter Education: ")
gender = input("Enter Gender: ")
age = input("Enter Age: ")
dob = input("Enter Date of Birth (dd-mm-yyyy): ")
current_address = input("Enter Current Address: ")
permanent_address = input("Enter Permanent Address: ")
job_preference = input("Enter Job Preference (enter the number corresponding to the job vacancy): ")

# Display entered details
print("\nEntered Details:")
print("Name: " + first_name + " " + last_name)
print("Email: " + email)
print("Contact Details: " + contact)
print("Marital Status: " + marital_status)
print("Education: " + education)
print("Gender: " + gender)
print("Age: " + age)
print("Date of Birth: " + dob)
print("Current Address: " + current_address)
print("Permanent Address: " + permanent_address)
print("Job Preference: " + job_vacancies.get(job_preference, "Invalid option"))

# Ask for confirmation
confirmation = input("\nDo you confirm that the above information is correct? (Y/N): ")
if confirmation.lower() == "y":
    print("\nThank you for submitting your application!")
else:
    print("\nPlease check your entered details and try again.")
