# Create a program with a predefined dictionary for a person: Including name, age, gender, address, and phone number.
# Ask the user what info they want to know about the person and print that to the associated key or print "info not found"

person = {
    "name": "Kris Kettendorf",
    "age": "34",
    "gender": "male",
    "address": "123 Yoohoo Blvd",
    "phone number": "876-543-2198", #how to get phone number if key is phone_number || phoneNumber?
}
Key = input("What information would you like to know about the person? ").lower()
result = person.get(Key, "infomration not available")
print(result)
# shift + command + p "run python..." to run file in terminal
