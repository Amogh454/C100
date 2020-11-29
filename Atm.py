class Atm(object):
    def __init__(self,atmcardno,pinNumber,bank,showlimit):
         self.atmcardno=atmcardno
         self.pinNumber=pin
         self.bank=bankname
         self.showlimit=showlimit

    def piniscorrect(self):
        print("Pin is correct")
    
    def showbalance(self):
        print("300000")

card=Atm("0101","4243","sbi","20000")
card.piniscorrect()
card.showbalance()
print(card.atmcardno)
print(card.pinNumber)