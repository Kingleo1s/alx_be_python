# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Base reminder message
reminder_message = f"Reminder: '{task}' is a {priority.upper()} priority task"

# Match Case for priority level
match priority:
