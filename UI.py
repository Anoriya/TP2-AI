# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Desktop\AI\TP2-AI\UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget

from classes import Predicat


class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 130, 71, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 100, 71, 21))
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(440, 130, 71, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 100, 141, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 250, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(140, 330, 631, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 310, 55, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(140, 410, 631, 51))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 380, 55, 16))
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(170, 260, 181, 20))
        self.radioButton.setObjectName("radioButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 30, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(140, 20, 411, 51))
        self.textEdit_5.setObjectName("textEdit_5")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(590, 80, 151, 31))
        self.toolButton.setObjectName("toolButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 130, 91, 31))
        self.label_5.setObjectName("label_5")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 260, 211, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 170, 141, 16))
        self.label_6.setObjectName("label_6")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(440, 200, 71, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 170, 71, 21))
        self.label_7.setObjectName("label_7")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(290, 200, 71, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 200, 91, 31))
        self.label_8.setObjectName("label_8")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(140, 510, 631, 51))
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(140, 480, 121, 16))
        self.label_9.setObjectName("label_9")
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(140, 600, 631, 51))
        self.textEdit_9.setObjectName("textEdit_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(140, 570, 55, 16))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.openFileNameDialog)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Valeur de x"))
        self.label_2.setText(_translate("MainWindow", "Valeur de y"))
        self.pushButton.setText(_translate("MainWindow", "Début"))
        self.label_3.setText(_translate("MainWindow", "Résultat"))
        self.label_4.setText(_translate("MainWindow", "Chemin"))
        self.radioButton.setText(_translate("MainWindow", "A star"))
        self.pushButton_2.setText(_translate("MainWindow", "Importer le fichier"))
        self.toolButton.setText(_translate("MainWindow", "Choisir l\'emplacement du log"))
        self.label_5.setText(_translate("MainWindow", "Initialisation"))
        self.radioButton_2.setText(_translate("MainWindow", "Recherche profendeur limité Itéartif"))
        self.label_6.setText(_translate("MainWindow", "Valeur de y"))
        self.label_7.setText(_translate("MainWindow", "Valeur de x"))
        self.label_8.setText(_translate("MainWindow", "But"))
        self.label_9.setText(_translate("MainWindow", "Règles appliqués"))
        self.label_10.setText(_translate("MainWindow", "Parcours"))

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Text files (*);;Python Files (*.txt)", options=options)
        self.textEdit_5.setText(fileName)

    def resoudre(self):
        EtatInit = Predicat('cruchesAetB',[self.textEdit.toPlainText(),self.textEdit2.toPlainText()],'fait')
        But = Predicat('cruchesAetB',[self.textEdit7.toPlainText(),self.textEdit6.toPlainText()],'')
        resolver = Resolver(self.textEdit_5.toPlainText(),)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
