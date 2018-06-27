import sys
from __UI import  TTTPY
from PyQt4 import QtGui

class ttt(QtGui.QMainWindow, TTTPY.Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connectUI()
        self.moves = 9
        self.filled = ['','','','','','','','','']
        self.deactivate()

    def connectUI(self):
        self.one.clicked.connect(self.get_11)
        self.two.clicked.connect(self.get_21)
        self.three.clicked.connect(self.get_31)
        self.one_2.clicked.connect(self.get_12)
        self.two_2.clicked.connect(self.get_22)
        self.three_2.clicked.connect(self.get_32)
        self.one_3.clicked.connect(self.get_13)
        self.two_3.clicked.connect(self.get_23)
        self.three_3.clicked.connect(self.get_33)
        self.choice_x.clicked.connect(self.mark_x)
        self.choice_o.clicked.connect(self.mark_o)

    def display_message(self, message):
        print message
        msgBox = QtGui.QMessageBox()
        msgBox.setText(message)
        msgBox.exec_()
        msgBox.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)

    def get_val_linedit(self):
        self.get_val = str(self.lineEdit.text("Choose your Mark"))

    def get_11(self):
        self.one.setText(QtGui.QApplication.translate("MainWindow", self.input_val , None, QtGui.QApplication.UnicodeUTF8))
        self.one.setEnabled(False)
        self.filled[0] = self.input_val
        self.TicTacToe()

    def get_21(self):
        self.two.setText(QtGui.QApplication.translate("MainWindow", self.input_val , None, QtGui.QApplication.UnicodeUTF8))
        self.two.setEnabled(False)
        self.filled[1] = self.input_val
        self.TicTacToe()

    def get_31(self):
        self.three.setText(QtGui.QApplication.translate("MainWindow", self.input_val, None, QtGui.QApplication.UnicodeUTF8))
        self.three.setEnabled(False)
        self.filled[2] = self.input_val
        self.TicTacToe()

    def get_12(self):
        self.one_2.setText(QtGui.QApplication.translate("MainWindow", self.input_val, None, QtGui.QApplication.UnicodeUTF8))
        self.one_2.setEnabled(False)
        self.filled[3] = self.input_val
        self.TicTacToe()

    def get_22(self):
        self.two_2.setText(QtGui.QApplication.translate("MainWindow", self.input_val, None, QtGui.QApplication.UnicodeUTF8))
        self.two_2.setEnabled(False)
        self.filled[4] = self.input_val
        self.TicTacToe()

    def get_32(self):
        self.three_2.setText(QtGui.QApplication.translate("MainWindow", self.input_val, None, QtGui.QApplication.UnicodeUTF8))
        self.three_2.setEnabled(False)
        self.filled[5] = self.input_val
        self.TicTacToe()

    def get_13(self):
        self.one_3.setText(QtGui.QApplication.translate("MainWindow", self.input_val, None, QtGui.QApplication.UnicodeUTF8))
        self.one_3.setEnabled(False)
        self.filled[6] = self.input_val
        self.TicTacToe()

    def get_23(self):
        self.two_3.setText(QtGui.QApplication.translate("MainWindow", self.input_val, None, QtGui.QApplication.UnicodeUTF8))
        self.two_3.setEnabled(False)
        self.filled[7] = self.input_val
        self.TicTacToe()

    def get_33(self):
        self.three_3.setText(QtGui.QApplication.translate("MainWindow", self.input_val, None, QtGui.QApplication.UnicodeUTF8))
        self.three_3.setEnabled(False)
        self.filled[8] = self.input_val
        self.TicTacToe()

    def mark_x(self):
        self.choice_x.setEnabled(False)
        self.choice_o.setEnabled(False)
        self.lineEdit.setText("You have choosen X mark !")
        self.p1 = "X"
        self.p2 = "O"
        self.activate()
        return self.TicTacToe()

    def mark_o(self):
        self.choice_x.setEnabled(False)
        self.choice_o.setEnabled(False)
        self.lineEdit.setText("You have choosen O mark !")
        self.p1 = "O"
        self.p2 = "X"
        self.activate()
        return self.TicTacToe()

    def TicTacToe(self):
        if self.p1 == "X":
            self.TicTacToe_X()
        else:
            self.TicTacToe_O()

    def TicTacToe_X(self):
        if self.moves >= 0:
            if self.moves%2 != 0:
                self.lineEdit.setText("Player1 Term !!! -- X")
                self.input_val = "X"
            else:
                self.lineEdit.setText("Player2 Term !!! -- O")
                self.input_val = "O"
            self.moves-=1
            self.checker()

    def TicTacToe_O(self):
        if self.moves >= 0:
            if self.moves % 2 != 0:
                self.lineEdit.setText("Player1 Term !!! -- O")
                self.input_val = "O"
            else:
                self.lineEdit.setText("Player2 Term !!! -- X")
                self.input_val = "X"
            self.moves-=1
            self.checker()

    def checker(self):
        null = ''
        ways = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in ways:
            if self.filled[i[0]] == self.filled[i[1]] == self.filled[i[2]] != null:
                winner = self.filled[i[0]]
                if winner == self.p1:
                    self.display_message("P1 won")
                    self.deactivate()
                    print "hi"
                elif winner == self.p2:
                    self.display_message("P2 Won")
                    self.deactivate()
                else:
                    pass
            if null not in self.filled:
                self.display_message("TIE")
                break
        return None

    def deactivate(self):
        self.one.setEnabled(False)
        self.one_2.setEnabled(False)
        self.one_3.setEnabled(False)
        self.two.setEnabled(False)
        self.two_2.setEnabled(False)
        self.two_3.setEnabled(False)
        self.three.setEnabled(False)
        self.three_2.setEnabled(False)
        self.three_3.setEnabled(False)

    def activate(self):
        self.one.setEnabled(True)
        self.one_2.setEnabled(True)
        self.one_3.setEnabled(True)
        self.two.setEnabled(True)
        self.two_2.setEnabled(True)
        self.two_3.setEnabled(True)
        self.three.setEnabled(True)
        self.three_2.setEnabled(True)
        self.three_3.setEnabled(True)

def main():
    app = QtGui.QApplication(sys.argv)
    myWindow = ttt(None)
    myWindow.show()
    app.exec_()

if __name__ == "__main__":
    main()
