# NovaSol IT Onboarding Script
import os
import datetime

# BUG 1: Fixed - Added the correct import datetime line


# BUG 2: Fixed - Using None as default parameter to avoid mutable default trap
def setup_workstation(software_name, installed_programs=None):
    if installed_programs is None:
        installed_programs = []
    installed_programs.append(software_name)
    return installed_programs


# BUG 3: Fixed - Using .get() method for safe dictionary access
office_locations = {"Engineering": "Building A", "Sales": "Building B"}

print("*** NovaSol IT Onboarding ***")
emp_name = input("Enter new employee name: ")
dept_name = input("Enter department (Engineering or Sales): ")

# Safe dictionary access with default value
location = office_locations.get(dept_name, "Remote Worker")

print("Setting up software...")

# Employee 1 gets Python
emp1_software = setup_workstation("Python")

# Employee 2 gets Excel - Now independent from emp1 due to bug fix
emp2_software = setup_workstation("Excel")

print("\n*** Setup Complete ***")

# BUG 4: Fixed - Added missing 'f' for f-string
print(f"Year: {datetime.date.today().year}")
print(f"Employee: {emp_name}")
print(f"Office Location: {location}")
print(f"Employee 2 Software Installed: {emp2_software}")

# Feature A: Folder Creation using os library
try:
    os.makedirs("onboarding_logs", exist_ok=True)
    print("\n✅ Created 'onboarding_logs' folder successfully!")
except Exception as e:
    print(f"\n❌ Error creating folder: {e}")