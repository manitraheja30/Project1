#importng files
import colored as colored

from send_message import send_message
from read_message import read_message
from addstatus import addstatus
from addfriend import add_friend
from globals import statusmsg
from  read_chat import read_chat
from addstatus import addstatus

#startchat() function definition
def startchat(name,age,rating):
    showmenu = True         #to display menu
    while showmenu:
        menuchoices = "What do you want to do?\n1) Add a status update\n" \
                      "2) Add a friend\n" \
                      "3) Send a secret message\n" \
                      "4) Read a secret message\n" \
                      "5) Read chats from a user\n" \
                      "6) Close the application\n"
        result = int(raw_input(menuchoices))

        #validating the menuchoice
        if result == 1:
            statusmsg=addstatus()
            print colored("Your Current status is: " + statusmsg, 'green')
        elif result == 2:
            # action
            no_of_friends = add_friend()
            print colored("You have %d friends " % (no_of_friends), 'green')
        elif (result == 3):
            send_message()
        elif (result == 4):
            read_message()
        elif result == 5:
            read_chat()
        elif result == 6:
            showmenu = False
        else:
            print colored("Sorry invalid option ",'red')