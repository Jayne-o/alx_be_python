# daily_reminder.py

# Prompt for user input task
task = input("Enter your task for today: ")
priority = input("What is the priority level? (high/medium/low): ").strip().lower()
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()

# Process the task using match-case priority
match priority:
    case "high":
        reminder = f"🔴 High priority task: {task}"
    case "medium":
        reminder = f"🟠 Medium priority task: {task}"
    case "low":
        reminder = f"🟢 Low priority task: {task}"
    case _:
        reminder = f"⚪ Unrecognized priority for task: {task}"
# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " — that requires immediate attention today!"

# Print the customized reminder using a loop for emphasis
for _ in range(1):
    print("\nYour Daily Reminder:")
    print(reminder)
