from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QTableWidget, QTableWidgetItem

import sys
from library import *

app = QtWidgets.QApplication([])
win = uic.loadUi("apartments.ui")

Gr = Grup()

# Начальное количество строк в таблице
win.tableWidget.setRowCount(0)

# Определение функции btnLoadTable
def btnLoadTable():
    # Очищаем таблицу перед загрузкой новых данных
    win.tableWidget.setRowCount(0)

    Gr.read_data_from_file("text.txt")  # Читаем данные из файла

    # Устанавливаем количество строк в таблице
    win.tableWidget.setRowCount(Gr.count)

    row = 0
    for x in Gr.A:
        # Записываем данные без номера строки
        win.tableWidget.setItem(row, 0, QTableWidgetItem(Gr.A[x].street))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(Gr.A[x].house))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(Gr.A[x].flat))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(Gr.A[x].rooms))
        win.tableWidget.setItem(row, 4, QTableWidgetItem(Gr.A[x].floor))
        # Добавляем номер строки слева от таблицы
        win.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(str(row + 1)))  # Номер строки
        row += 1

    # Удаляем пустые строки
    for row in range(win.tableWidget.rowCount() - 1, -1, -1):
        isEmpty = True
        for col in range(win.tableWidget.columnCount()):
            item = win.tableWidget.item(row, col)
            if item is not None and item.text() != "":
                isEmpty = False
                break
        if isEmpty:
            win.tableWidget.removeRow(row)

btnLoadTable()  # Вызов функции для загрузки данных при запуске
def addNewRow():
    # Получаем текущее количество строк
    rowCount = win.tableWidget.rowCount()
    # Добавляем новую строку (увеличиваем количество строк)
    win.tableWidget.setRowCount(rowCount + 1)

    # Устанавливаем значения в новой строке (индекс последней строки):
    win.tableWidget.setItem(rowCount, 0, QTableWidgetItem("Новая улица"))
    win.tableWidget.setItem(rowCount, 1, QTableWidgetItem("Новый дом"))
    win.tableWidget.setItem(rowCount, 2, QTableWidgetItem("Новая квартира"))
    win.tableWidget.setItem(rowCount, 3, QTableWidgetItem("Новые комнаты"))
    win.tableWidget.setItem(rowCount, 4, QTableWidgetItem("Новый этаж"))

    # Добавляем номер строки слева от таблицы:
    win.tableWidget.setVerticalHeaderItem(rowCount, QTableWidgetItem(str(rowCount + 1)))

    # Настройка ширины столбцов:
    win.tableWidget.setColumnWidth(1, 90)
    win.tableWidget.setColumnWidth(2, 110)
    win.tableWidget.setColumnWidth(3, 110)


def clearTable():
    # Очищаем таблицу, устанавливая количество строк в 0
    win.tableWidget.setRowCount(0)


def deleteRow():
    selected_row = win.tableWidget.currentRow()

    if selected_row != -1 and selected_row in Gr.A:
        del Gr.A[selected_row]  # Удаляем запись из Gr.A
        Gr.count -= 1  # Обновляем Gr.count
        win.tableWidget.removeRow(selected_row)  # Удаляем строку из таблицы


def enableEditing():
    win.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)


def disableEditing():
    win.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


def saveChanges():
    # Перезаписываем данные из таблицы в файл
    # НЕ ОЧИЩАЕМ Gr.A: Gr.A = {}

    for row in range(win.tableWidget.rowCount()):
        # Извлекаем данные из таблицы
        street = win.tableWidget.item(row, 0).text()
        house = win.tableWidget.item(row, 1).text()
        flat = win.tableWidget.item(row, 2).text()
        rooms = win.tableWidget.item(row, 3).text()
        floor = win.tableWidget.item(row, 4).text()

        # Добавляем новые данные в список
        Gr.A[row] = Apartment(street, house, flat, rooms, floor)

    Gr.write_data_to_file("text.txt")  # Сохраняем изменения в файл

win.pushButton.clicked.connect(btnLoadTable)
win.pushButton_2.clicked.connect(clearTable)
win.pushButton_3.clicked.connect(addNewRow)
win.pushButton_4.clicked.connect(deleteRow)
win.pushButton_5.clicked.connect(enableEditing)
win.pushButton_6.clicked.connect(saveChanges)

win.show()
sys.exit(app.exec_())
