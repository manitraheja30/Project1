from globals import friends,Spy
from termcolor import colored
import re
# add new friends
def add_friend():
    newfriend ={
        "name": "",
        "salutation" : "",
        "age" : 0,
        "rating" : 0.0,
        "status" : False

    }
    tempcheck = True  # temporary variable
    # Validation Using Regex
    patternsalutation = '^Mr|Ms$'
    patternname = '^[A-Za-z][A-Za-z\s]+$'
    patternage = '^[0-9]+$'
    patternrating = '^[0-9]+\.[0-9]$'
    # Validating Each Values Using Regular Expression
    while tempcheck:
        newfriend["salutation"] = raw_input("What should we call them (Mr./Mrs.): ")
        if (re.match(patternsalutation, newfriend["salutation"]) != None):
            tempcheck = False
        else:
            print colored("Enter Again!!!!", 'red')

    tempcheck = True
    while tempcheck:
        newfriend["name"] = raw_input("Pleae add your friend\s name: ")
        if (re.match(patternname, newfriend["name"]) != None):
            tempcheck = False
        else:
            print colored("Enter Again!!!!", 'red')

    newfriend['name'] = newfriend['salutation'] + "" + newfriend['name']

    tempcheck = True
    while tempcheck:
        newfriend['age'] = (raw_input("Age? "))
        if (re.match(patternage, newfriend['age']) != None):
            tempcheck = False
            newfriend['age'] = int(raw_input("Age? "))
        else:
            print colored("Enter Again!!!!", 'red')

    tempcheck = True  # temporary variable
    while tempcheck:
        newfriend['rating'] = (raw_input("Rating? "))
        if (re.match(patternrating, newfriend['rating']) != None):
            tempcheck = False
            newfriend['rating'] = float(raw_input("Rating? "))
        else:
            print colored("Enter Again!!!!", 'red')





    # validation

    if len(newfriend["name"]) > 0 and newfriend["age"] > 12 and newfriend["age"] < 50 and newfriend["rating"] >=Spy["rating"]:
        friends.append(newfriend)
        print colored("Friend added! ",'green')

    else:
        print colored("Sorry invalid entry.Can\'t add a spy",'red')

    # returning number of friends
    return len(friends)