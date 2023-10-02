number = input("Type a number: ")

# handling a successful entry
try:
    number = float(number)
    print("This number is: ", number)
# this is where we catch an error or invalid entry
except:
    print("Invalid number")
    number = input("Type a number: ")
    # trying to reprompt and then execute the 'try' block
# pandas...quest bootcamp...starter project...geopanda...htmx...automation in python
# CGI consulting web dev in dublin...homeland security data engineer/developer role 