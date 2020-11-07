################################################################################
##                                                                            ##
## Author: Marek Sokol                                                        ##
## Made with: QtDesigner and PySide2                                          ##
##                                                                            ##
################################################################################

import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from ui_spinners import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.i = 0
        self.start()

    def start(self):
        self.i += 1
        self.i %= 360
        self.update_spinner_1(self.i)
        self.update_spinner_2(self.i)
        self.update_spinner_3(self.i)
        QTimer.singleShot(10, self.start)

    def update_spinner_3(self, angle):
        style = f"""
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{-angle}, 
                stop:0 #689F38, 
                stop:0.454545 #8BC34A, 
                stop:0.784091 #C5E1A5, 
                stop:0.886364 rgba(255, 255, 255, 255), 
                stop:1 rgba(255, 255, 255, 255));
                border-radius: 85px;
                """
        self.ui.circle_outer_3.setStyleSheet(style)

    def update_spinner_2(self, angle):
        style_outer = f"""
                border-radius: 85px;
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{-angle}, 
                stop:0.4 #fff, stop:0.3999 #f44336);
                """
        style_inner = f"""
                border-radius: 70px;
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{180 - angle * 2}, 
                stop:0.4 #fff, stop:0.3999 #f44336);
                """
        self.ui.circle_outer_2.setStyleSheet(style_outer)
        self.ui.circle_inner_2.setStyleSheet(style_inner)

    def update_spinner_1(self, angle):
        style = f"""
             	border-radius: 85px;
             	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{-angle}, 
             	stop:0.3 #DFDFDF, 
             	stop:0.2999 #3F51B5);
                """
        self.ui.circle_outer_1.setStyleSheet(style)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
