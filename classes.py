#Class definition for cashbox which holds 100,50,20,10,5,2,1,0.25,0.10 and 0.05 values.
#Float expected
class Cashbox:
    def __init__(self,hundred,fifty,twenty,ten,five,two,one,quarter,dime,nickel):
        self.hundred = hundred
        self.fifty = fifty
        self.twenty = twenty
        self.ten = ten
        self.five = five
        self.two = two
        self.one = one
        self.quarter = quarter
        self.dime = dime
        self.nickel = nickel

#Return total money in cashbox
    def getTotal(self):
        total = self.hundred + self.fifty + self.twenty + self.ten + self.five + self.two + self.one + self.quarter + self.dime + self.nickel
        return total

   
#Report class for different values needed to complete End of Day report.    
class Report:
    def __init__(self, netsales, quantityorders, tipamount, expecteddeposit):
        self.NetSales = netsales
        self.QuantityOfOrders = quantityorders
        self.TipAmount = tipamount
        self.ExpectedDeposit = expecteddeposit
