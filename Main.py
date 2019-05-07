import sys
from PyQt5 import QtWidgets
from Frm_Calculadora import Frm_Calculadora

if __name__ == "__main__":
    calcu = QtWidgets.QApplication(sys.argv)
    execu = Frm_Calculadora()
    execu.show()
    sys.exit(calcu.exec_())