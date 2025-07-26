from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("The date after", days, "days will be:", formatted_future)

def main():
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate future date
    try:
        days_input = int(input("Enter number of days to add to today's date: "))
        calculate_future_date(days_input)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

if __name__ == "__main__":
    main()
days_input = int(input("Enter the number of days to add to the current date: "))

