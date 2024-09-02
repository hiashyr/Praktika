from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
import sys
from library import *

class Apartment:
    def __init__(self, street, house, flat, rooms, floor):
        self.street = street
        self.house = house
        self.flat = flat
        self.rooms = rooms
        self.floor = floor

class Group:
    def __init__(self):
        self.A = []  # Список квартир
        self.count = 0

    def read_data_from_file(self, filename):
        # Ваш код для чтения данных из файла и заполнения self.A
        pass

    def write_data_to_file(self, filename):
        # Ваш код для записи данных self.A в файл
        pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Здесь исправлен вызов конструктора родительского класса
        uic.loadUi("apartments.ui", self)
        self.Gr = Group()

        # Начальное количество строк в таблице
        self.tableWidget.setRowCount(0)

        # Подключение кнопок к методам
        self.btnLoadTable.clicked.connect(self.load_table)
        self.btnAddRow.clicked.connect(self.add_new_row)
        self.btnClearTable.clicked.connect(self.clear_table)
        self.btnDeleteRow.clicked.connect(self.delete_row)
        self.btnSave.clicked.connect(self.save_changes)
        self.btnEnableEditing.clicked.connect(self.enable_editing)
        self.btnDisableEditing.clicked.connect(self.disable_editing)

        # Загрузка данных при запуске
        self.load_table()

    def load_table(self):
        """Загружает данные в таблицу из списка квартир."""
        self.tableWidget.setRowCount(0)
        self.Gr.read_data_from_file("text.txt")  # Читаем данные из файла
        self.tableWidget.setRowCount(len(self.Gr.A))

        for row, apartment in enumerate(self.Gr.A):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(apartment.street))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(apartment.house))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(apartment.flat))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(apartment.rooms))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(apartment.floor))
            self.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(str(row + 1)))  # Номер строки

        # Удаляем пустые строки, если такие есть
        for row in range(self.tableWidget.rowCount() - 1, -1, -1):
            is_empty = all(self.tableWidget.item(row, col) is None or self.tableWidget.item(row, col).text() == ""
                           for col in range(self.tableWidget.columnCount()))
            if is_empty:
                self.tableWidget.removeRow(row)

    def add_new_row(self):
        """Добавляет новую строку в таблицу."""
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(rowCount + 1)

        # Устанавливаем значения в новой строке
        self.tableWidget.setItem(rowCount, 0, QTableWidgetItem("Новая улица"))
        self.tableWidget.setItem(rowCount, 1, QTableWidgetItem("Новый дом"))
        self.tableWidget.setItem(rowCount, 2, QTableWidgetItem("Новая квартира"))
        self.tableWidget.setItem(rowCount, 3, QTableWidgetItem("Новые комнаты"))
        self.tableWidget.setItem(rowCount, 4, QTableWidgetItem("Новый этаж"))
        self.tableWidget.setVerticalHeaderItem(rowCount, QTableWidgetItem(str(rowCount + 1)))

        # Настройка ширины столбцов
        self.tableWidget.setColumnWidth(1, 90)
        self.tableWidget.setColumnWidth(2, 110)
        self.tableWidget.setColumnWidth(3, 110)

    def clear_table(self):
        """Очищает таблицу."""
        self.tableWidget.setRowCount(0)

# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())