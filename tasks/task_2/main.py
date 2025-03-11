def convert_temperature(temp_str):
    temp_str = temp_str.strip()  # Remove any extra spaces

    if temp_str[-1].lower() == "c":  # Detect Celsius
        celsius = float(temp_str[:-1])  # Extract numeric value
        fahrenheit = (celsius * 9 / 5) + 32  # Convert to Fahrenheit
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    elif temp_str[-1].lower() == "f":  # Detect Fahrenheit
        fahrenheit = float(temp_str[:-1])  # Extract numeric value
        celsius = (fahrenheit - 32) * 5 / 9  # Convert to Celsius
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

    else:
        print(
            "Invalid input. Please enter a temperature followed by 'C' or 'F' (e.g., 30C or 86F)."
        )


# Taking input from the user
temp_input = input("Enter temperature (e.g., 25C or 77F): ")
convert_temperature(temp_input)
