import time
import random
loopvar = True
response = ""
toDolist = []
searching = False
thing = ""
removing = ""
removeloop = False
fullToDoList = []
mistake = ["s","z","w","n","k","j","l","t","f","g","d","e","x","v",","," "]
mistakeAdd = ["s","z"]
mistakeShow = ["x","d","v"," "]
mistakeRemove = ["e","f","t","g"]
mistakeQuit = ["w"]
mistakeMenu = ["n","j","k","l",","]
mistakeLoop = False
answer = ""
listingOutViaNumbers = 0
face = 0
print("_______________________\n|      To Do List     |\n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\n|       ~ ~~~ ~~~     |\n|       ~~ ~~~~~      |\n|       ~~~~ ~ ~~     |\n|       ~~ ~~~~~      |\n|       ~~ ~~~ ~~     |\n|       ~ ~ ~~~ ~~    |\n|       ~~ ~~~~ ~     |\n|       ~~ ~~~ ~~     |\n|       ~ ~~ ~~~~     |\n|       ~~~~~ ~~      |\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n")
while loopvar == True:
    print("\n_________\n| Menu  |\n¯¯¯¯¯¯¯¯¯\n")
    time.sleep(0.05)
    print("Add [a]")
    time.sleep(0.04)
    print("Check Off List [r]")
    time.sleep(0.03)
    print("Show list [c]")
    time.sleep(0.02) 
    print("Quit [q]")
    time.sleep(0.01)

    # your response
    response=input().strip().lower()

    #checking what you put
    if len(response) > 1 or len(response) < 0 or response != "q" and response != "a" and response != "r" and response != "c" and response != "m" and response not in mistake:
        # wrong answer
        print("thats not one of the options")
        time.sleep(random.randint(3,5))
        print("\ntype in the things in the []'s when in the menu\n\n")
    
    elif response in mistake:
        print("is '" + response + "' what you ment to put? [y/n]")
        while mistakeLoop == True:
            answer = input().strip().lower()

            if answer == "yes":
                answer = "y"
            elif answer == "no":
                answer = "n"
            if answer == "y":
                print("ok, taking you back to the menu because that is not one of the options")
                mistakeLoop = False
            elif answer == "n":
                if response in mistakeQuit:
                    print("placeholder")

                    mistakeLoop = False
                elif response in mistakeRemove:
                    print("placeholder")

                    mistakeLoop = False
                elif response in mistakeAdd:
                    print("placeholder")

                    mistakeLoop = False
                elif response in mistakeShow:
                    print("placeholder")

                    mistakeLoop = False
                elif response in mistakeMenu:
                    print("placeholder")

                    mistakeLoop = False
            else:
                print("its a yes/no question")
    
    elif response == "q":
        if len(fullToDoList)>0:
            print("\n to do list:")
            listingOutViaNumbers=0
            while listingOutViaNumbers < len(fullToDoList):
                print(f"{listingOutViaNumbers + 1}. {fullToDoList[listingOutViaNumbers]}")
                listingOutViaNumbers += 1

        # exiting the code
        print("\nBye, have a good day")
        loopvar=False
    
    elif response == "r":
        # removing something from the list 
        if len(toDolist)>0:
            print("\nWhat would you like to remove? ('c' or 'cancel' to cancel)")
            removeloop=True
            while removeloop==True:
                listingOutViaNumbers=0
                while listingOutViaNumbers < len(toDolist):
                    print(f"{listingOutViaNumbers + 1}. {toDolist[listingOutViaNumbers]}")
                    listingOutViaNumbers += 1
                    
                removing = input().strip()
                if removing == "c" or removing == "cancel":
                    print("alright, taking you back to the menu\n\n")
                    removeloop = False
                else:
                    if removing in toDolist:
                        toDolist.remove(removing)
                        print(removing, "was successfully checked off\n\n")
                        removeloop=False
                    else:
                        print("\n", "'"+removing+"'","is not on the list currently")
                        print("\nplease select something on the list")
                    
        else:
            print("there isnt anything on the to-do list rn")
    
    elif response == "a":

        # adding something to the list
        print("\nWhat would you like to add? ['c' or 'cancel' to cancel]")
        varInput = input().strip()
        if varInput == "c" or varInput == "cancel":
            print("alright, raking you back to the menu\n\n")
        else:
            if varInput in toDolist:
                print("thats already on the list\n\n")
            else:
                toDolist.append(varInput)
                fullToDoList.append(varInput)
                print(varInput, "was successfuly addded\n\n")
    
    elif response == "c":
        # seeing everything you've added 
        if len(toDolist)>0:
            print("\nWhich would you like to see? (put the number or 'all', 'c' to cancel)")
            finding = True
            while finding==True:
                if len(toDolist) == 1:
                    print ("\nThere is",len(toDolist),"item on the list")
                else:
                    print ("\nThere is",len(toDolist),"items on the list")
                thing = input().strip().lower()
                if thing.isnumeric():
                    thing = int(thing)
                    if thing > len(toDolist):
                        print("\nThats not on the list")
                    else:
                        thing = thing - 1
                        print("\nthis is the one you chose:",toDolist[thing])
                        finding = False
                elif thing == "all":
                    print("\nHeres the full list:")
                    listingOutViaNumbers=0
                    while listingOutViaNumbers < len(toDolist):
                        print(f"{listingOutViaNumbers + 1}. {fullToDoList[listingOutViaNumbers]}")
                        listingOutViaNumbers += 1
                        print("\n")
                        finding = False
                elif thing == "c":
                    print("alright, taking you back to the menu\n\n")
                    finding = False
                else:
                    print("\n'~'\n")
        else:
            print("There isnt anything to do on the list")
    
    elif response == "m":
        face = random.randint(1,10)
        if face==1:
            print(":/")
        if face==2:
            print(":(")
        if face==3:
            print(":v")
        if face==4:
            print(":^")
        if face==5:
            print(":1")
        if face==6:
            print(":s")
        if face==7:
            print(":|")
        if face==8:
            print(":l")
        if face==9:
            print(":c")
        if face==10:
            print(":[")
