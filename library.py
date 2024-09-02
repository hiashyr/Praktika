class Apartment:
    def __init__(self, street, house, flat, rooms, floor):
        """Инициализирует квартиру с данными о ее адресе и характеристиках."""
        self.street = street
        self.house = house
        self.flat = flat
        self.rooms = rooms
        self.floor = floor

    def __str__(self):
        """Возвращает строковое представление квартиры."""
        return f"{self.street} {self.house} {self.flat} {self.rooms} {self.floor}"


class Group:
    def __init__(self):
        """Инициализирует пустую группу квартир."""
        self.apartments = {}  # Словарь для хранения данных о квартирах
        self.count = 0  # Количество квартир

    def read_data_from_file(self, filename):
        """Считывает данные из файла и создает объекты квартир."""
        self.apartments = {}
        self.count = 0

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()  # Разделяем по пробелам
                if len(parts) == 5:
                    street, house, flat, rooms, floor = parts
                    self.apartments[self.count] = Apartment(street, house, flat, rooms, floor)
                    self.count += 1
                else:
                    print(f"Некорректные данные в строке: {line.strip()}")

    def write_data_to_file(self, filename):
        """Записывает данные о квартирах в файл."""
        with open(filename, "w", encoding="utf-8") as file:
            for key, apartment in self.apartments.items():  # Итерация по ключам словаря
                file.write(f"{apartment}\n")  # Используем метод __str__ класса Apartment
