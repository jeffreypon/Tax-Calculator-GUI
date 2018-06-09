import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic #works for pyqt5
#from PyQt4 import QtCore, QtGui, uic #works for pyqt4. library structures differ from pyqt5. qtcore/qtgui in qtwidgets in pyqt5


qtCreatorFile = "GUI_SalesTax.ui"  # Enter GUI form file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#class MyApp(QtGui.QMainWindow, Ui_MainWindow):     #pyqt4 version
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        #QtGui.QMainWindow.__init__(self)           #pyqt4 version
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.calculatetax)

    def calculatetax(self):
        price = int(self.price_box.toPlainText())
        tax = (self.tax_rate.value())
        total_price = price + ((tax / 100) * price)
        total_price_string = "The total price with tax is: " + str(total_price)
        self.results_window.setText(total_price_string)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


