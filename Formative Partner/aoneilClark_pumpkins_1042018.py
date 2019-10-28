'''Ambrose O'Neil'''
'''Programming 1'''
'''10/15/2018'''
'''Partner Wilson's Farm'''

def main():
    weight=0
    pumpkinWeightTotal=0
    pumpkinCostTotal=0
    print "Welcome to Wilson's Farm! The local store for all of your pumpkin needs!"
    cashorcredit = raw_input("Would you like to pay with Cash or Credit? ")
    if cashorcredit == "Cash" or cashorcredit == "cash":
        answer = True
    elif cashorcredit == "Credit" or cashorcredit == "credit":
        answer = False
    boughtPumpkins=input("How many pumpkins do you wish to buy? ")
    for i in range(boughtPumpkins):
        pumpkinCost= 0
        name = raw_input("What is the name of a family member? ")
        weight = input("How much does the pumpkin weigh? ")
        pumpkinType = raw_input("What type of pumpkin does " +str(name)+ " want? (Big, Sugar, Specialty, or Tiny) ")
        if pumpkinType == "Big" or pumpkinType == "big":
            price= 0.59
            pumpkinCost = weight * price
        elif pumpkinType == "Sugar" or pumpkinType == "sugar":
            price= 0.99
            pumpkinCost = weight * price
        elif pumpkinType == "Specialty" or pumpkinType == "specialty":
            price= 0.99
            pumpkinCost = weight * price
        elif pumpkinType == "Tiny" or pumpkinType == "tiny":
            price= 1.99
            pumpkinCost = weight * price
        else:
            print  "This isn't a valid input"
            quit 
        pumpkinWeightTotal += weight 
        pumpkinCostTotal += pumpkinCost
        print name,"got a",pumpkinType,"pumpkin that weighed",weight,"pounds and the cost was",pumpkinCost
    print "The total weight of all the pumpkins is %s." % (pumpkinWeightTotal)
    print "The total cost of all the pumpkins is %s. " % (pumpkinCostTotal) 
    print "The average weight of all the pumpkins are %s. " % (pumpkinWeightTotal/boughtPumpkins)
    print "The average cost of all the pumpkins are %s. " % (round(pumpkinCostTotal/boughtPumpkins,2))
    print "Thanks for shopping at Wilson's Farm where we have the best assortment of pumpkins"
main()