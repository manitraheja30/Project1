#import statements
from spydetails import spy
from startchat import startchat

print "Welcome to Spy Chat. It's good to have you"
question = raw_input("Would you like to continue as "+spy["salutation"]+""+spy["name"]+" (Y/N): ")    #default user or new user
if question == "y" or question == "Y":
    startchat(spy["name"],spy["age"],spy["rating"])

elif question == "N" or question == "n":
    name=raw_input("Please enter your name: ")                          #variable for spy name
    salutation=raw_input("What should we call you Mr. or Mrs.?: ")      #variable for salutation

    if len(name) > 0:
        age = 0               #spy age
        rating = 0.0          #spy rating
        status = False        #spy status
        print "Welcome "+salutation+" "+name
        print "We would like to know more about you"
        age=int(raw_input("Please enter your age: "))           #input spy age

        if (age < 12 or age > 50):                              #condition to check valid age of spy
            print "Sorry please enter valid age."

        else:
            rating=float(raw_input("Please enter your rating: "))   #input spy rating

            if rating > 4.5:                                        #print messages according to spy rating
                print "Great ace!!"
            elif rating > 3.5 and rating <= 4.5 :
                print "Nice work!!!"
            elif rating > 2.5 and rating <= 3.5 :
                print "Keep it up!!!"

            else :
                print "Work hard!!!"

            print "Thanks for all the info,here are your details: "
            print "Name: %s |Age: %s |Rating: %s "%(name,str(age),str(rating))  #final details of spy
            startchat(name, age, rating)

    else:
        print "Sorry Invalid user name.Please try again."

else:
    print "Not valid Input.Please try again."