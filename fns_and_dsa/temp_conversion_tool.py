# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)  # Validate numeric value

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted:.2f}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        print("Invalid temperature. Please enter a numeric value.")
        print(f"Error detail: {ve}")

if __name__ == "__main__":
    main()
