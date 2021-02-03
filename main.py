from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtCore
import random
import pa
import sys
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = pa.Ui_MainWindow()
        self.ui.setupUi(self)

        with open('animals.txt', 'w') as file:
            animals = requests.get('https://gist.githubusercontent.com/atduskgreg/3cf8ef48cb0d29cf151bedad81553a54/raw/82f142562cf50b0f6fb8010f890b2f934093553e/animals.txt')
            file.write(animals.text)

        with open('plants.txt', 'w') as file:
            plants = requests.get('https://gist.githubusercontent.com/researchranks/ffe24c33df30e64f51271ddec83b4af6/raw/0e15dabe9b54611288cf92f93e1bfa288e150448/flower-and-plant-names.csv')
            file.write(plants.text)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.ui.pushButton_3.clicked.connect(lambda: self.showMinimized())
        self.ui.lineEdit.setPlaceholderText("Animals")
        self.ui.lineEdit_2.setPlaceholderText("Plants")

        self.ui.pushButton_4.clicked.connect(self.animal_generate)
        self.ui.pushButton_5.clicked.connect(self.plant_generate)


    def animal_generate(self):
        file = open('animals.txt', 'r')
        animals = file.readlines()
        self.ui.lineEdit.setText(random.choice(animals))

    def plant_generate(self):
        file = open('./plants.txt', 'r')
        plants = file.readlines()
        self.ui.lineEdit_2.setText(random.choice(plants))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    appctxt = ApplicationContext()
    MyWindow = MainWindow()
    MyWindow.show()
    sys.exit(appctxt.app.exec_())
