# daily_reminder.py

# Prompt for user input with exact required wording
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ").strip().lower()

# Process the task using match-case
match priority:
    case "high":
        reminder = f"🔴 High priority task: {task}"
    case "medium":
        reminder = f"🟠 Medium priority task: {task}"
    case "low":
        reminder = f"🟢 Low priority task: {task}"
    case _:
        reminder = f"⚪ Unrecognized priority for task: {task}"
# Modify reminder if time-sensitive
if time_bound.lower() == "yes":
    reminder += " — that requires immediate attention today!"

# Display the customized reminder
print("\nYour Daily Reminder:")
print(reminder)
