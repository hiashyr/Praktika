class Apartment:
    def __init__(self, street, house, flat, rooms, floor):
        self.street = street
        self.house = house
        self.flat = flat
        self.rooms = rooms
        self.floor = floor


class Grup:
    def __init__(self):
        self.A = {}  # Словарь для хранения данных об квартирах
        self.count = 0  # Количество квартир

    def read_data_from_file(self, filename):
        self.A = {}
        self.count = 0
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()  # Разделяем по пробелам
                if len(parts) == 5:
                    street, house, flat, rooms, floor = parts
                    self.A[self.count] = Apartment(street, house, flat, rooms, floor)
                    self.count += 1
                else:
                    print(f"Некорректные данные в строке: {line.strip()}")

    def write_data_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for key, apartment in self.A.items():  # Итерация по ключам словаря
                file.write(f"{apartment.street} {apartment.house} {apartment.flat} {apartment.rooms} {apartment.floor}\n")