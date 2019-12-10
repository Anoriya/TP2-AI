# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Kalelt'has\Desktop\My GL4\AI\Tp AI\UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget



class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.chainageAvant = ChainageAvant()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 170, 171, 61))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 140, 71, 21))
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(490, 170, 181, 61))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 140, 141, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 250, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(140, 330, 631, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 310, 55, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(140, 410, 631, 271))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 380, 55, 16))
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(190, 270, 181, 20))
        self.radioButton.setObjectName("radioButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 30, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(140, 20, 411, 51))
        self.textEdit_5.setObjectName("textEdit_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.openFileNameDialog)
        self.pushButton.clicked.connect(self.Chainage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "key"))
        self.label_2.setText(_translate("MainWindow", "Valeur de but"))
        self.pushButton.setText(_translate("MainWindow", "Début"))
        self.label_3.setText(_translate("MainWindow", "Résultat"))
        self.label_4.setText(_translate("MainWindow", "log"))
        self.radioButton.setText(_translate("MainWindow", "Staurer la base de faits"))
        self.pushButton_2.setText(_translate("MainWindow", "Importer le fichier"))

    def Chainage(self):

        boolean = self.chainageAvant.StartChainge(self.textEdit.toPlainText(), self.textEdit_2.toPlainText(),
                                                  self.textEdit_4, self.textEdit_5.toPlainText(),
                                                  self.radioButton.isChecked())
        if boolean:
            self.textEdit_3.setText("But Atteint")
        else:
            if self.radioButton.isChecked():
                self.textEdit_3.setText("Base de faits saturée")
            else:
                self.textEdit_3.setText("But non atteint, Base de faits saturée")

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Text files (*);;Python Files (*.txt)", options=options)
        self.textEdit_5.setText(fileName)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
