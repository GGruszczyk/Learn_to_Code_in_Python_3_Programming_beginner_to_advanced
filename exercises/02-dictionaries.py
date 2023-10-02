# also known as an object or associative array; can hold any datatype
person = {
    "firstName": "John",
    "lastName": "Green",
    "birthyear": 1980,
    "countryOfBirth": "Canada",
}
type(person)
person["firstName"]

# changing an attribute
person["birthyear"] = 1979  # changing birthYear

# adding a new element or property
person["maritalStatus"] = "Married"

# to grab properties
person.get("children", "invalid property")

# reference a property by Key
Key = person("firstName")

# erase data from a dictionary
person.clear()
