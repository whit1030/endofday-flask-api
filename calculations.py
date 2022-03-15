from classes import Cashbox

#Function to check the value of cash variable and add it to class variable.
# def addValue(cashbox: Cashbox, cash: float):
#     if (cash == 100):
#         cashbox.hundred += cash
#     elif(cash == 50):
#         cashbox.fifty += cash
#     elif(cash == 20):
#         cashbox.twenty += cash
#     elif(cash == 10):
#         cashbox.ten += cash
#     elif(cash == 5):
#         cashbox.five += cash
#     elif(cash == 2):
#         cashbox.two += cash
#     elif(cash == 1): 
#         cashbox.one += cash
#     elif(cash == 0.25): 
#         cashbox.quarter += cash
#     elif(cash == 0.1): 
#         cashbox.dime += cash
#     elif(cash == 0.05): 
#         cashbox.nickel += cash
#     else:
#         print('Could not deposit $' + str(cash)+ '  must be either 100,50,20,10,5,2,1,0.25,0.10,0.05')

# #Method to remove value from CashDrawer in 100,50,20,10,5,2,1,0.25,0.10 and 0.05 increments.
# def subtractValue(cashbox: Cashbox, cash: float):
#     if ((cash == 100) and (cashbox.hundred > 0) ):
#         cashbox.hundred -= cash
#     elif(cash == 50 and (cashbox.fifty > 0)):
#         cashbox.fifty -= cash
#     elif(cash == 20 and (cashbox.twenty > 0)):
#         cashbox.twenty -= cash
#     elif(cash == 10 and (cashbox.ten > 0)):
#         cashbox.ten -= cash
#     elif(cash == 5 and (cashbox.five > 0)):
#         cashbox.five -= cash
#     elif(cash == 2 and (cashbox.two > 0)):
#         cashbox.two -= cash
#     elif(cash == 1 and (cashbox.one > 0)): 
#         cashbox.one -= cash
#     elif(cash == 0.25 and (cashbox.quarter > 0)): 
#         cashbox.quarter -= cash
#     elif(cash == 0.1 and (cashbox.dime > 0)): 
#         cashbox.dime -= cash
#     elif(cash == 0.05 and (cashbox.nickel > 0)): 
#         cashbox.nickel -= cash
#     else:
#         print('Could not deposit $' + str(cash)+ '  must be either 100,50,20,10,5,2,1,0.25,0.10,0.05')


#Function that takes original cashbox Cashbox class and float tips to generate tips Cashbox
#Function called in depositCashboxGenerator to make deposit Cashbox

def CashboxWizard(cashbox: Cashbox, tips: float):
    calculatedCashbox = Cashbox(0,0,0,0,0,0,0,0,0,0)

    #Iterate through each value and remove from
    while((tips >= 100) and (cashbox.hundred > 0)):
        tips -= 100
        cashbox.hundred -= 100
        calculatedCashbox.hundred += 100
    while((tips >= 50) and (cashbox.fifty > 0)):
        tips -= 50
        cashbox.fifty -= 50
        calculatedCashbox.fifty += 50
    while((tips >= 20) and (cashbox.twenty > 0)):
        tips -= 20
        cashbox.twenty -= 20
        calculatedCashbox.twenty += 20
    while((tips >= 10) and (cashbox.ten > 0)):
        tips -= 10
        cashbox.ten -= 10
        calculatedCashbox.ten += 10
    while((tips >= 5) and (cashbox.five > 0)):
        tips -= 5
        cashbox.five -= 5
        calculatedCashbox.five += 5
    while((tips >= 2) and (cashbox.two > 0)):
        tips -= 2
        cashbox.two -= 2
        calculatedCashbox.two += 2
    while((tips >= 1) and (cashbox.one > 0)):
        tips -= 1
        cashbox.one -= 1
        calculatedCashbox.one += 1
    while((tips >= 0.25) and (cashbox.quarter > 0)):
        tips -= 0.25
        cashbox.quarter -= 0.25
        calculatedCashbox.quarter += 0.25
    while((tips >= 0.1) and (cashbox.dime > 0)):
        tips -= 0.1
        cashbox.dime -= 0.1
        calculatedCashbox.dime += 0.1
    while((tips >= 0.05) and (cashbox.nickel > 0)):
        tips -= 0.05
        cashbox.nickel -= 0.05
        calculatedCashbox.nickel += 0.05
    #Check for remaining balance error
    if(tips == 0):
        return calculatedCashbox
    else:
        print("Deposit not equal to zero, cashbox needs more change." + tips)
    
#function to take a calculatedCashbox with seperated tips and remove the float to generate a deposit Cashbox
def depositCashboxWizard(calculatedCashbox: Cashbox):
    onHand = calculatedCashbox.getTotal() - 100
    depositCashbox = CashboxWizard(calculatedCashbox, onHand)
    return depositCashbox