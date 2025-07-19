# pattern_drawing.py

# Prompt user for a positive integer
try:
    size = int(input("Enter the size of the pattern: "))

    if size > 0:
        row = 0
        while row < size:
            for col in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1
    else:
        print("⚠️ Please enter a positive integer.")

except ValueError:
    print("⚠️ Invalid input. Please enter a valid integer.")
