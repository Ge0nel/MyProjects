import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from converter import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
         
    def init_UI(self): # Маленькая дороботка интерфейса и функция, которая активирует конвертор

        self.setWindowTitle("Ковертер валют")
        self.setWindowIcon(QIcon("banknote.png"))

        self.ui.inputCurrency.setPlaceholderText("Из валюты:")
        self.ui.inputAmount.setPlaceholderText("Кол-во валюты")
        self.ui.outputCurrency.setPlaceholderText("В валюту:")
        self.ui.outputAmount.setPlaceholderText("Результат:")
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self): # Функция, которая конвертирует валюты
        c = CurrencyConverter() # Экземпляр класса CurrencyConverter
        # получаем текст из полей ввода
        inputCurrency = self.ui.inputCurrency.text() # тип валюты, из которой будем конвертировать
        inputAmount = int(self.ui.inputAmount.text()) # кол-во валюты
        outputCurrency = self.ui.outputCurrency.text() # в какую валюту будем конвертировать

        outputAmount = round(c.convert(inputAmount, "%s" % (inputCurrency), "%s" % (outputCurrency)), 2) # результат

        self.ui.outputAmount.setText("%s" % (outputAmount)) # Выводим результат, как value для окна ввода

app = QtWidgets.QApplication([]) # создание окна
application = CurrencyConv()  # экземляр класса CurrencyConv для дальнейшего отображения
application.show() # работа с экземпляром в окне

sys.exit(app.exec()) # выход
