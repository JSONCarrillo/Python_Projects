from abc import ABC, abstractmethod

upgrades = {
        "Combat" : "$1.7m",
        "R&D" : "$1.1m",
        "Intel" : "$1.5m"
    }

class Motherbase(ABC):
    def purchaseReceipt(self, key):
        if key == 'Combat':
            print(f"Your purchase for Combat Platform is {upgrades[key]}")
        elif key == 'R&D':
            print(f"Your purchase for R&D Platform is {upgrades[key]}")
        elif key == 'Intel':
            print(f"Your purchase for Intel Platform is {upgrades[key]}")
        else:
            print("Your purchase will cost you: ", key)
    #Passes argument, but will not say what data type it will be
    @abstractmethod
    def payment(self, key):
        pass

class mbPurchase(Motherbase):
    #defines how to implement payment function from its parent class
    def payment(self, key):
        if key == 'Combat':
            print(f"Your {upgrades[key]} purchase for the Combat Platform is 1m short")
        elif key == 'Intel':
            print(f"Your {upgrades[key]} purchase for the Combat Platform is 1m short")
        elif key == 'R&D':
            print(f"Your {upgrades[key]} purchase for the Combat Platform is 1m short")
        else:
            print("Purchase Complete!")
            
obj = mbPurchase()

obj.purchaseReceipt('Combat')
obj.payment('Intel')
