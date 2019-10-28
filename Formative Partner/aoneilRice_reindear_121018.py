import random

def christmasList():
    listItems = ["Dasher","Dancer","Prancer","Vixen","Comet","Cupid","Donner","Blitzen"]
    print listItems
    listItems.append("Rudolph")
    print listItems
    listItems.remove("Blitzen")
    print listItems
    print listItems[-1]
    print listItems[0:8]
    print("\n")
christmasList()

def christmasImport():
    times=1
    christmas=1
    guess=0
    listItems = ["Dasher","Dancer","Prancer","Vixen","Comet","Cupid","Donner","Blitzen","Rudolph"]
    favRein = random.choice(listItems) 
    print listItems    
    for i in range(times):
        while christmas != favRein:          
            rein = raw_input("What is santa's favorite reindeer? ")
            if rein == favRein:
                print "You Win!"
                guess+=1
            else:
                print "Oof, try again!"
                guess+=1
            tryAgain=raw_input("Would you like to try again? (Yes/No) ")
            if tryAgain == "Yes" or tryAgain == "yes":
                continue
            elif tryAgain == "No" or tryAgain == "no":
                break
            else:
                print "That is not a valid statement"
                quit
    print "Santa's favorite reindeer was "+str(favRein)+". It took you "+str(guess)+" guesses."
christmasImport()