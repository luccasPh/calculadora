# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caculadora.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from os import path
import sys
import platform


class Ui_Cal(object):
    def setupUi(self, Form):
        self.imag = path.join(path.dirname(__file__), "img")
        Form.setEnabled(True)
        Form.resize(641, 341)
        Form.setMinimumSize(QtCore.QSize(641, 341))
        Form.setMaximumSize(QtCore.QSize(641, 341))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget {\n" "background-color:rgb(85, 85, 85);\n" "}")
        self.btn0 = QtWidgets.QPushButton(Form)
        self.btn0.setGeometry(QtCore.QRect(280, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btn0.setFont(font)
        self.btn0.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(103,103,103); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btn0.setObjectName("btn0")
        self.btn1 = QtWidgets.QPushButton(Form)
        self.btn1.setGeometry(QtCore.QRect(280, 240, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(103,103,103); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btn1.setObjectName("btn1")
        self.btn4 = QtWidgets.QPushButton(Form)
        self.btn4.setGeometry(QtCore.QRect(280, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(103,103,103); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btn4.setObjectName("btn4")
        self.btn7 = QtWidgets.QPushButton(Form)
        self.btn7.setGeometry(QtCore.QRect(280, 140, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btn7.setFont(font)
        self.btn7.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(103,103,103); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(Form)
        self.btn8.setGeometry(QtCore.QRect(370, 140, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btn8.setFont(font)
        self.btn8.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(103,103,103); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btn8.setObjectName("btn8")
        self.btnPont = QtWidgets.QPushButton(Form)
        self.btnPont.setGeometry(QtCore.QRect(370, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnPont.setFont(font)
        self.btnPont.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(103,103,103); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnPont.setObjectName("btnPont")
        self.btn2 = QtWidgets.QPushButton(Form)
        self.btn2.setGeometry(QtCore.QRect(370, 240, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(103,103,103); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btn2.setObjectName("btn2")
        self.btn5 = QtWidgets.QPushButton(Form)
        self.btn5.setGeometry(QtCore.QRect(370, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btn5.setFont(font)
        self.btn5.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(103,103,103); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btn5.setObjectName("btn5")
        self.btnMult = QtWidgets.QPushButton(Form)
        self.btnMult.setGeometry(QtCore.QRect(550, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnMult.setFont(font)
        self.btnMult.setStyleSheet(
            "QPushButton {\n"
            "background-color:rgb(63,63,63); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnMult.setObjectName("btnMult")
        self.btnIgual = QtWidgets.QPushButton(Form)
        self.btnIgual.setGeometry(QtCore.QRect(460, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnIgual.setFont(font)
        self.btnIgual.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(204,0,0); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnIgual.setObjectName("btnIgual")
        self.btnDivi = QtWidgets.QPushButton(Form)
        self.btnDivi.setGeometry(QtCore.QRect(550, 140, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnDivi.setFont(font)
        self.btnDivi.setStyleSheet(
            "QPushButton {\n"
            "background-color:rgb(63,63,63); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnDivi.setObjectName("btnDivi")
        self.btnMais = QtWidgets.QPushButton(Form)
        self.btnMais.setGeometry(QtCore.QRect(550, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnMais.setFont(font)
        self.btnMais.setStyleSheet(
            "QPushButton {\n"
            "background-color:rgb(63,63,63); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnMais.setObjectName("btnMais")
        self.btn9 = QtWidgets.QPushButton(Form)
        self.btn9.setGeometry(QtCore.QRect(460, 140, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btn9.setFont(font)
        self.btn9.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(103,103,103); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btn9.setObjectName("btn9")
        self.btnSubi = QtWidgets.QPushButton(Form)
        self.btnSubi.setGeometry(QtCore.QRect(550, 240, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnSubi.setFont(font)
        self.btnSubi.setStyleSheet(
            "QPushButton {\n"
            "background-color:rgb(63,63,63); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnSubi.setObjectName("btnSubi")
        self.btn3 = QtWidgets.QPushButton(Form)
        self.btn3.setGeometry(QtCore.QRect(460, 240, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(103,103,103); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btn3.setObjectName("btn3")
        self.btn6 = QtWidgets.QPushButton(Form)
        self.btn6.setGeometry(QtCore.QRect(460, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btn6.setFont(font)
        self.btn6.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(103,103,103); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btn6.setObjectName("btn6")
        self.btnLn = QtWidgets.QPushButton(Form)
        self.btnLn.setGeometry(QtCore.QRect(190, 140, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnLn.setFont(font)
        self.btnLn.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnLn.setObjectName("btnLn")
        self.btnRaiz = QtWidgets.QPushButton(Form)
        self.btnRaiz.setGeometry(QtCore.QRect(190, 240, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRaiz.setFont(font)
        self.btnRaiz.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnRaiz.setText("")
        icon = QtGui.QIcon.fromTheme("raiz")
        self.btnRaiz.setIcon(QtGui.QIcon(path.join(self.imag, "raizquadrada.png")))
        self.btnRaiz.setIconSize(QtCore.QSize(25, 25))
        self.btnRaiz.setObjectName("btnRaiz")
        self.btnEleva = QtWidgets.QPushButton(Form)
        self.btnEleva.setGeometry(QtCore.QRect(190, 290, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEleva.setFont(font)
        self.btnEleva.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnEleva.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("asasasasa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.btnEleva.setIcon(QtGui.QIcon(path.join(self.imag, "exponecial.png")))
        self.btnEleva.setIconSize(QtCore.QSize(25, 25))
        self.btnEleva.setObjectName("btnEleva")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 621, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "QLabel {\n"
            "background-color : rgb(225,245,169);\n"
            "qproperty-alignment: 'AlignVCenter | AlignRight';\n"
            "border: 1px solid gray;\n"
            "}\n"
            "\n"
            "background-color : white;"
        )
        self.label.setObjectName("label")
        self.btnDivi_2 = QtWidgets.QPushButton(Form)
        self.btnDivi_2.setGeometry(QtCore.QRect(190, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnDivi_2.setFont(font)
        self.btnDivi_2.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnDivi_2.setObjectName("btnDivi_2")
        self.btnLimpa = QtWidgets.QPushButton(Form)
        self.btnLimpa.setGeometry(QtCore.QRect(550, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnLimpa.setFont(font)
        self.btnLimpa.setStyleSheet(
            "QPushButton {\n"
            "background-color:rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnLimpa.setObjectName("btnLimpa")
        self.btnPocet = QtWidgets.QPushButton(Form)
        self.btnPocet.setGeometry(QtCore.QRect(460, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnPocet.setFont(font)
        self.btnPocet.setStyleSheet(
            "QPushButton {\n"
            "background-color:rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnPocet.setObjectName("btnPocet")
        self.btnPi = QtWidgets.QPushButton(Form)
        self.btnPi.setGeometry(QtCore.QRect(10, 190, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnPi.setFont(font)
        self.btnPi.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnPi.setText("")
        icon = QtGui.QIcon.fromTheme("pi")
        self.btnPi.setIcon(QtGui.QIcon(path.join(self.imag, "pi.png")))
        self.btnPi.setIconSize(QtCore.QSize(25, 25))
        self.btnPi.setShortcut("")
        self.btnPi.setAutoDefault(False)
        self.btnPi.setDefault(False)
        self.btnPi.setFlat(False)
        self.btnPi.setObjectName("btnPi")
        self.btnEnes = QtWidgets.QPushButton(Form)
        self.btnEnes.setGeometry(QtCore.QRect(10, 140, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnEnes.setFont(font)
        self.btnEnes.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnEnes.setIconSize(QtCore.QSize(50, 50))
        self.btnEnes.setObjectName("btnEnes")
        self.btnParet1 = QtWidgets.QPushButton(Form)
        self.btnParet1.setGeometry(QtCore.QRect(370, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnParet1.setFont(font)
        self.btnParet1.setStyleSheet(
            "QPushButton {\n"
            "background-color:rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnParet1.setObjectName("btnParet1")
        self.btnParet2 = QtWidgets.QPushButton(Form)
        self.btnParet2.setGeometry(QtCore.QRect(280, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnParet2.setFont(font)
        self.btnParet2.setStyleSheet(
            "QPushButton {\n"
            "background-color:rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnParet2.setObjectName("btnParet2")
        self.btnFatori = QtWidgets.QPushButton(Form)
        self.btnFatori.setGeometry(QtCore.QRect(100, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnFatori.setFont(font)
        self.btnFatori.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnFatori.setObjectName("btnFatori")
        self.btnLog = QtWidgets.QPushButton(Form)
        self.btnLog.setGeometry(QtCore.QRect(190, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnLog.setFont(font)
        self.btnLog.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnLog.setObjectName("btnLog")
        self.btnExp = QtWidgets.QPushButton(Form)
        self.btnExp.setGeometry(QtCore.QRect(100, 240, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnExp.setFont(font)
        self.btnExp.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnExp.setObjectName("btnExp")
        self.btnTan = QtWidgets.QPushButton(Form)
        self.btnTan.setGeometry(QtCore.QRect(100, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnTan.setFont(font)
        self.btnTan.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnTan.setObjectName("btnTan")
        self.btnCos = QtWidgets.QPushButton(Form)
        self.btnCos.setGeometry(QtCore.QRect(100, 140, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnCos.setFont(font)
        self.btnCos.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnCos.setObjectName("btnCos")
        self.btnSen = QtWidgets.QPushButton(Form)
        self.btnSen.setGeometry(QtCore.QRect(100, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnSen.setFont(font)
        self.btnSen.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnSen.setObjectName("btnSen")
        self.btnGrau = QtWidgets.QPushButton(Form)
        self.btnGrau.setGeometry(QtCore.QRect(10, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnGrau.setFont(font)
        self.btnGrau.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnGrau.setObjectName("btnGrau")
        self.btnRadi = QtWidgets.QPushButton(Form)
        self.btnRadi.setGeometry(QtCore.QRect(10, 240, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnRadi.setFont(font)
        self.btnRadi.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnRadi.setObjectName("btnRadi")
        self.btnRam = QtWidgets.QPushButton(Form)
        self.btnRam.setGeometry(QtCore.QRect(10, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.btnRam.setFont(font)
        self.btnRam.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgb(63,63,63); color: white;\n"
            "border: 1px solid gray;\n"
            "}\n"
            "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
            "}"
        )
        self.btnRam.setObjectName("btnRam")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(10, 0, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setStyleSheet(
            "QLabel {\n"
            "background-color : rgb(85,85,85); color: white;\n"
            "qproperty-alignment: 'AlignVCenter | AlignRight';\n"
            "}\n"
            "\n"
            "background-color : white;"
        )
        self.label2.setObjectName("label")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculadora"))
        self.btn0.setText(_translate("Form", "0"))
        self.btn1.setText(_translate("Form", "1"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn7.setText(_translate("Form", "7"))
        self.btn8.setText(_translate("Form", "8"))
        self.btnPont.setText(_translate("Form", "."))
        self.btn2.setText(_translate("Form", "2"))
        self.btn5.setText(_translate("Form", "5"))
        self.btnMult.setText(_translate("Form", "x"))
        self.btnIgual.setText(_translate("Form", "="))
        self.btnDivi.setText(_translate("Form", "÷"))
        self.btnMais.setText(_translate("Form", "+"))
        self.btn9.setText(_translate("Form", "9"))
        self.btnSubi.setText(_translate("Form", "-"))
        self.btn3.setText(_translate("Form", "3"))
        self.btn6.setText(_translate("Form", "6"))
        self.btnLn.setText(_translate("Form", "ln"))
        self.label.setText(_translate("Form", "0"))
        self.btnDivi_2.setText(_translate("Form", "+/-"))
        self.btnLimpa.setText(_translate("Form", "AC"))
        self.btnPocet.setText(_translate("Form", "%"))
        self.btnEnes.setText(_translate("Form", "e"))
        self.btnParet1.setText(_translate("Form", ")"))
        self.btnParet2.setText(_translate("Form", "("))
        self.btnFatori.setText(_translate("Form", "x!"))
        self.btnLog.setText(_translate("Form", "log"))
        self.btnExp.setText(_translate("Form", "exp"))
        self.btnTan.setText(_translate("Form", "tan"))
        self.btnCos.setText(_translate("Form", "cos"))
        self.btnSen.setText(_translate("Form", "sen"))
        self.btnGrau.setText(_translate("Form", "grau"))
        self.btnRadi.setText(_translate("Form", "radi"))
        self.btnRam.setText(_translate("Form", "Ram"))
