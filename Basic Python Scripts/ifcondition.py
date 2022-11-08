temperature = float(input("Please enter body temperature: "))

if  temperature<98.6:
    print("Hypothermia")
elif temperature==98.6:
    print("Normal Temperature")
else:
    print("High Temperature")