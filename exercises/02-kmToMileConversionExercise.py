print("Km to Miles Converter")
print("This program converts a number from Kilometers to Miles")

numToConvert = float(input("Please enter a number to convert"))

kilometerToMileConversion = numToConvert / 1.609344

print(numToConvert, "miles equals", round(kilometerToMileConversion, 4), "kilometers")        
