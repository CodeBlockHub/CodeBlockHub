import temperature_conversion as tc

while True:
    print("Temperature Conversion Utility")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Celsius to Kelvin")
    print("4: Kelvin to Celsius")
    print("5: Exit")

    choice = input("Choose an option (1/2/3/4/5): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}° Celsius is {tc.celsius_to_fahrenheit(celsius)}° Fahrenheit.")

    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}° Fahrenheit is {tc.fahrenheit_to_celsius(fahrenheit)}° Celsius.")

    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}° Celsius is {tc.celsius_to_kelvin(celsius)} Kelvin.")

    elif choice == '4':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} Kelvin is {tc.kelvin_to_celsius(kelvin)}° Celsius.")

    elif choice == '5':
        break

    else:
        print("Invalid choice.")