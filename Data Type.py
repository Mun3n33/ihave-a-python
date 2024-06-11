# Datatype

number = 78  # Int
num = 45.09  # Float
greeting = "How are you doing"
Is_Programming_Interesting = True  # bool
devices = ["laptop", "tablet", "computer", "phone"]  # list
browser = ("opera", "chrome", "firefox", "safari", "brave")  # tuple
countries = {"Kenya", "Uganda", "Tanzania"}  # Set
employees = {
    "firstname": "Jane",
    "Age": 29,
    "Nationality": "Kenyan",
    "EmailAddress": "jane@gmail.com"
}  # Dictionary

print(Is_Programming_Interesting)
print(num)
print(countries)
print(devices)
print(employees["firstname"])

# Determining a data type
print(type(countries))
print(type(employees
))

# Typecasting is the process of converting one data type to another
print(int(num))
print(float(number))
