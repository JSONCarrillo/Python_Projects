class Motherbase:
    def __init__(self):
        self.__teams = {
                "Espionage Team" : ['Big Boss', 'Quiet', 'DD', 'D-Horse'],
                "Motherbase Team" : ['Ocelot', 'Kaz', 'Huey']
            }
    def getData(self, data):
        print(self.__teams[data])
        
    def _addData(self, team, members):
        self.__teams[team] = members

obj = Motherbase()

obj.getData("Espionage Team")
obj._addData("Brig",['Eli', 'Skull Face'])
obj.getData("Brig")
