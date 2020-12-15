#Diamond Dog parent class
class diamond_Dog:
    name = 'John'
    code_Name = 'Big Boss'
    Rank = 'S++'

    def diamondDogLog(self):
        entry_name = input("what is your name? " )
        entry_code = input("What is your code name? ").title()
        entry_rank = input("What is your rank? ")
        if (entry_code == self.code_Name and entry_rank != ''):
            print(f"Welcome to the Diamond Dogs {entry_code}!")
        else:
            print("Initiaiton error, please try again.")

#child class for diamond dogs who are on the R&D team
class r_And_D(diamond_Dog):
    team_Number = 6473
    specialization = 'Research and Development'

    def diamondDogLog(self):
        team_code = input("What is your code name? ").title()
        entry_pin = int(input("What is your entry pin? "))
        if (team_code == self.code_Name and entry_pin == self.team_Number):
            print(f"{team_code} Is now entering the R&D platform")
        else:
            print("You are not on this team. Access Denied.")

#child class for diamond dogs who are on the combat team
class combat_Team(diamond_Dog):
    combat_pin = 8675309
    combat_Tours = 12
    combat_Training = True

    def diamondDogLog(self):
        pin_Req = int(input("What is your Combat Info Pin? "))
        if (pin_Req == self.combat_pin):
            print(f"{self.code_Name} this is your combat stats: \
                    Combat Tours: {self.combat_Tours} \
                    CQC Training: {self.combat_Training}")
        else:
            print("You are not on this team. Access Denied.")

dDog = diamond_Dog()
rDevelopment = r_And_D()
combatTeam = combat_Team()

combatTeam.diamondDogLog()
