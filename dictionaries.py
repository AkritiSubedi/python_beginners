# with this curly braces we can define dictionaries
customer = {
    "name": "Akriti Subedi ",
    "age": 20,
    "is_verified": True
}
customer["birthdate"] = "feb 4 2001"
print(customer["age"])
print(customer["name"])
print(customer["is_verified"])
print(customer["birthdate"])
print(customer.get("Father name"))



phone = input (" Phone:")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "FIve",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!")
print(output)
