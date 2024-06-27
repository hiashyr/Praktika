from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QTableWidget, QTableWidgetItem

import sys
from library import *

app = QtWidgets.QApplication([])
win = uic.loadUi("студенты.ui")

Gr = Grup()

# Начальное количество строк в таблице
win.tableWidget.setRowCount(0)


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
    # Получаем выбранную строку
    selected_row = win.tableWidget.currentRow()

    # Если строка выбрана
    if selected_row != -1:
        # Удаляем строку
        win.tableWidget.removeRow(selected_row)


def enableEditing():
    win.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)


def disableEditing():
    win.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


# Делаем таблицу нередактируемой изначально
disableEditing()

# Подключаем функцию deleteRow к кнопке
win.pushButton_4.clicked.connect(deleteRow)

win.pushButton.clicked.connect(btnLoadTable)
win.pushButton_3.clicked.connect(addNewRow)
# Подключаем функцию clearTable к pushButton_2
win.pushButton_2.clicked.connect(clearTable)

# Подключаем функцию enableEditing к pushButton_5
win.pushButton_5.clicked.connect(enableEditing)

win.show()
sys.exit(app.exec())
