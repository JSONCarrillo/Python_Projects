#creates class of Motherbase
class Motherbase:
    #initializes teams variable
    def __init__(self):
        #saves teams as a library to utilizes multiple teams with multiple
        #with multiple members saved as an array
        self.__teams = {
                "Espionage Team" : ['Big Boss', 'Quiet', 'DD', 'D-Horse'],
                "Motherbase Team" : ['Ocelot', 'Kaz', 'Huey']
            }
    #function to print the data selected
    def getData(self, data):
        print(self.__teams[data])

    #function that adds data to the __teams library
    def _addData(self, team, members):
        self.__teams[team] = members

#saves class as an object
obj = Motherbase()

#calls get data function to see what's inside the given dataset
obj.getData("Espionage Team")
#adds to library
obj._addData("Brig",['Eli', 'Skull Face'])
#calls to view the active data
obj.getData("Brig")
