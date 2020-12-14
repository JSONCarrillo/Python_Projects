#Diamond Dog parent class
class diamond_Dog:
    name = ''
    code_Name = ''
    Rank = 'S+'

#child class for diamond dogs who are on the R&D team
class r_And_D(diamond_Dog):
    team_Number = 001
    specialization = 'Research and Development

#child class for diamond dogs who are on the combat team
class combat_Team(diamond_Dog):
    combat_Tours = 12
    combat_Training = True
