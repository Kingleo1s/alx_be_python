# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Begin building the reminder message
reminder_message = ""

# Use match-case to respond based on priority
match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder_message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder_message = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder_message = f"⚠️ '{task}' has an unknown priority level."
        print(reminder_messa_
