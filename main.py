import sys
from PyQt5 import QtWidgets
from frm_cal import Frm_Cal

if __name__ == "__main__":
    calcu = QtWidgets.QApplication(sys.argv)
    execu = Frm_Cal()
    execu.show()
    sys.exit(calcu.exec_())