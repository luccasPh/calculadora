import sys
from PyQt5 import QtWidgets
from cProfile import label
from ui_cal import Ui_Cal
from log_cal import Log_Cal

class Frm_Cal(QtWidgets.QMainWindow,Ui_Cal,Log_Cal):
    def __init__(self):
        super().__init__()
        self.conta = ""
        self.new_conta = ""
        self.operadores = "+-x÷"
        self.setupUi(self)
        self.show()
        self.zero = True
        self.backup_Texto = ""
        self.nao_opera = True
        self.muda_operado = False
        self.numy = True
        self.ponto = False
        self.resul = False
        self.ram = "0"

        self.btn0.clicked.connect(self.digitos_tela)
        self.btn1.clicked.connect(self.digitos_tela)
        self.btn2.clicked.connect(self.digitos_tela)
        self.btn3.clicked.connect(self.digitos_tela)
        self.btn4.clicked.connect(self.digitos_tela)
        self.btn5.clicked.connect(self.digitos_tela)
        self.btn6.clicked.connect(self.digitos_tela)
        self.btn7.clicked.connect(self.digitos_tela)
        self.btn8.clicked.connect(self.digitos_tela)
        self.btn9.clicked.connect(self.digitos_tela)
        self.btnPocet.clicked.connect(self.digitos_tela)
        self.btnParet1.clicked.connect(self.digitos_tela)
        self.btnParet2.clicked.connect(self.digitos_tela)
        self.btnLn.clicked.connect(self.digitos_tela)
        self.btnLog.clicked.connect(self.digitos_tela)
        self.btnSen.clicked.connect(self.digitos_tela)
        self.btnCos.clicked.connect(self.digitos_tela)
        self.btnTan.clicked.connect(self.digitos_tela)
        self.btnExp.clicked.connect(self.digitos_tela)
        self.btnRadi.clicked.connect(self.digitos_tela)
        self.btnGrau.clicked.connect(self.digitos_tela)
        self.btnFatori.clicked.connect(self.digitos_tela)
        self.btnEnes.clicked.connect(self.digitos_tela)
        self.btnPont.clicked.connect(self.digitos_tela)
        self.btnDivi_2.clicked.connect(self.muda_sinal)
        self.btnRam.clicked.connect(self.digitos_tela)

        self.btnRaiz.clicked.connect(lambda:self.digitos_tela("raiz"))
        self.btnEleva.clicked.connect(lambda:self.digitos_tela("eleva"))
        self.btnPi.clicked.connect(lambda:self.digitos_tela("pi"))

        self.btnMais.clicked.connect(self.operadores_tela)
        self.btnSubi.clicked.connect(self.operadores_tela)
        self.btnMult.clicked.connect(self.operadores_tela)
        self.btnDivi.clicked.connect(self.operadores_tela)

        self.btnLimpa.clicked.connect(self.limpar_tela)
        self.btnIgual.clicked.connect(self.resultado)
               
    def resultado(self):
        pa = 0
        pe = 0
        texto = " "+self.label.text() + " "
        self.conta = " "
        i = 0
        while i < len(texto):
            if texto[i] == "(":
                pe += 1
                self.conta += texto[i]
                i += 1
            elif texto[i] == ")":
                pa += 1
                self.conta += texto[i]
                i += 1
            elif texto[i] == "R":
                self.conta += self.ram
                i += 3
            else:
                self.conta += texto[i]
                i += 1
        if pa == pe:
            self.label2.setText(self.conta + " =")
            self.operacao()
            self.calcular()
            self.label.setText(str(self.new_conta))
            self.resul = True
            self.zero = True
            if "." in self.label.text():
                self.ponto = True
            else:
                self.ponto = False

    def limpar_tela(self):
        if self.resul:
            self.ram = self.label.text()
            self.label2.setText("Ram = "+self.ram)
        tela = self.label.text()
        try:
            if tela[len(tela)-1] == " ":
                new_tela = tela[:len(tela)-3]
            elif tela[len(tela)-3] == "l":
                new_tela = tela[:len(tela)-3]
            elif tela[len(tela)-3] == "o":
                new_tela = tela[:len(tela)-4]
            elif tela[len(tela)-2] == "√":
                new_tela = tela[:len(tela)-2]
            elif tela[len(tela)-3] == "e":
                new_tela = tela[:len(tela)-4]
            elif tela[len(tela)-2] == "s":
                new_tela = tela[:len(tela)-4]
            elif tela[len(tela)-4] == "t":
                new_tela = tela[:len(tela)-4]
            elif tela[len(tela)-2] == "p":
                new_tela = tela[:len(tela)-4]
            elif tela[len(tela)-2] == "i":
                new_tela = tela[:len(tela)-5]
            elif tela[len(tela)-2] == "u":
                new_tela = tela[:len(tela)-5]
            elif tela[len(tela)-1] == "m":
                new_tela = tela[:len(tela)-3]
            else:
                 new_tela = tela[:len(tela)-1]
        except:
             new_tela = tela[:len(tela)-1]
        try:
            if new_tela[len(new_tela)-1] == "(":
                self.nao_opera = False
        except:
            o=1
        if "." not in new_tela:
            self.ponto = False
        if new_tela == "" or self.resul or new_tela == "0":
            self.label.setText("0")
            self.zero = True
            self.resul = False

        else:
            self.label.setText(new_tela)
            self.zero = False
        
    def operadores_tela(self):
        if self.resul:
            self.ram = self.label.text()
            self.label2.setText("Ram = "+self.ram)
            self.resul = False

        if self.sender().text() == "-":
            self.nao_opera = True
        if self.nao_opera:
            butao = self.sender().text()
            if self.muda_operado:
                novo_Texto = self.backup_Texto + butao
                self.label.setText(novo_Texto)
            else:
                self.backup_Texto = self.label.text()
                novo_Texto = self.label.text() + " " + butao + " "
                self.label.setText(novo_Texto)
                self.muda_operado = True
                self.zero = False
                self.resul = False
                self.ponto = False
    
    def muda_sinal(self):
        if self.label.text()[0] == " - ":
            self.label.setText(""+self.label.text()[1:])
        else:
            self.label.setText(" - "+self.label.text()[0:])

    def digitos_tela(self,value):
        but = self.sender()
        if but.text() == "ln":
            butao = "ln("
            self.muda_operado = False
            self.nao_opera = False
        elif but.text() == "x!":
            if not self.muda_operado and self.nao_opera:
                butao = "!"
                self.muda_operado = False
                self.nao_opera = True
                self.zero = False
            else:
                butao = ""
                self.nao_opera = False
                self.zero = False
        elif but.text() == "log":
            butao = "log("
            self.muda_operado = False
            self.nao_opera = False
        elif but.text() == "sen":
            butao = "sen("
            self.muda_operado = False
            self.nao_opera = False
        elif but.text() == "cos":
            butao = "cos("
            self.muda_operado = False
            self.nao_opera = False
        elif but.text() == "tan":
            butao = "tan("
            self.muda_operado = False
            self.nao_opera = False
        elif but.text() == "exp":
            butao = "exp("
            self.muda_operado = False
            self.nao_opera = False
        elif but.text() == "radi":
            butao = "radi("
            self.muda_operado = False
            self.nao_opera = False
        elif but.text() == "grau":
            butao = "grau("
            self.muda_operado = False
            self.nao_opera = False
        elif value == "raiz":
            butao = "√("
            self.muda_operado = False
            self.nao_opera = False
        elif value == "eleva":
            butao = "^"
            self.zero = False
            self.muda_operado = False
            self.nao_opera = True
        elif value == "pi":
            butao = "π"
        elif but.text() == ".":
            if self.label.text()[len(self.label.text())-1] in self.operadores or self.ponto:
                butao = ""
                self.zero = False
            else:
                butao = "."
                self.muda_operado = False
                self.nao_opera = False
                self.ponto = True
                self.zero = False
        elif but.text() == "%":
            if not self.muda_operado and self.nao_opera:
                butao = "%"
                self.muda_operado = False
                self.nao_opera = True
                self.zero = False
            else:
                butao = ""
                self.nao_opera = False
                self.zero = False
        else:
            butao = but.text()
            if but.text() == "(":
                 self.nao_opera = False
                 self.muda_operado = False
            elif but.text() == ")" and self.muda_operado:
                butao = ""
            else:
                self.muda_operado = False
                self.nao_opera = True

        if self.resul:
            self.ram = self.label.text()
            self.label2.setText("Ram = "+self.ram)
            self.resul = False

        if self.zero:
            self.label.setText(butao)
            self.zero = False
            self.ponto = False
        else:
            novoText = self.label.text()+butao
            self.label.setText(novoText)

