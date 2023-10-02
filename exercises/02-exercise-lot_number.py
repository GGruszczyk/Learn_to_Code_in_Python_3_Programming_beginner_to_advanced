# Create a program to print out sections of a lot number: "037-00901-00027"
# Country Code - Product Number - Batch Number

# my attempt
# ask for lot number
# lotNumber = input("Exercise #2: Please provide a lot number- 3 digit country code, 5 digit product code, and 5 digit batch number ex: 123-45678-90123")
# print("Country code:" + lotNumber[0:2], "Product code:" + lotNumber[3:8], "Batch number:" + lotNumber[-5:])


# Solution:
lot_number = "037-00901-00027"

print("Country code:", lot_number[:3])  # start at beginning until 3rd index
print("Product code:", lot_number[4:9])  # start at 4-9
print("Batch number:", lot_number[10:])  # start at 10 until finished
