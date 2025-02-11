def convert_temperatures(temperatures, val):
    """
    Convert a list of temperatures between Celsius and Fahrenheit.
    Example: convert_temperatures([0, 100], "F") should return [32, 212]
    """
    # Your code here!
    converted = []

    for temp in temperatures:
        if  val == "F":
            converted.append((temp * 9/5) + 32)
        elif val == "C":
            converted.append((temp - 32) * 5/9)
        else:
            raise ValueError("Invalid conversion type. Use 'F' for Fahrenheit or 'C' for Celsius.")

    return converted



temperatures = [0, 100, 37, -40]

val = input("Enter 'C' to convert to Celsius or 'F' to convert to Fahrenheit: ").strip().upper()
ans = convert_temperatures(temperatures, val)

print(f"The converted {val} temperatures are : ", ans)

