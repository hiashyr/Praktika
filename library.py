class Person:
    def __init__(self, street, house, flat, rooms, floor):
        self.street = street
        self.house = house
        self.flat = flat
        self.rooms = rooms
        self.floor = floor

    """
    def getPerson_forTable(self):
        w = []
        print(self.fam+' '+self.name+' '+self.otchestvo)
        x = self.fam+' '+self.name+' '+self.otchestvo
        w.append(x)
        w.append(self.year)
        w.append(self.city)
        w.append(self.sb_inf)
        w.append(self.sb.math)
        print(w) 
        return w
    """

class Grup:
    def __init__(self):
        self.A = {}
        self.count = 0

    def __str__(self):
        s = ''
        for x in range(len(self.A)):  
            if x in self.A: 
                s += f'Person {x+1}:\n'
                s += str(self.A[x])
                s += '\n'
        return s



    def read_data_from_file(self, filename):
        self.A = {}
        x = 0
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line[-1] == '\n' : line = line[:-1] 
                parts = line.strip().split(" ")

                self.A[x] = Person(parts[0], parts[1], parts[2], parts[3],  parts[4])

                x += 1
                self.count += 1