# Temperature converter between Celsius and Fahrenheit
# Temperature will be rounded to the nearest integer
def fahrenheit_to_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) * 5/9)
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = round((celsius * 9/5) + 32)
    return fahrenheit

choice = input("Is the current temperature in (C)elsius or (F)ahrenheit? ").upper()

if choice == 'F':
    fahrenheit = float(input("What is the temperature in Fahrenheit?: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit is about {celsius} \u00b0Celsius")
elif choice == 'C':
    celsius = float(input("What is the temperature in Celsius?: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius is about {fahrenheit} \u00b0Fahrenheit")
elif choice == 'K':
    print("Kelvin is not supported in this program. Please use Celsius or Fahrenheit.")
else:
    print("Invalid input. Please enter 'C' or 'F' for your current temperature scale .")