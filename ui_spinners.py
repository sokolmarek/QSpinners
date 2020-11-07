# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_spinners.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 200)
        MainWindow.setMinimumSize(QSize(800, 200))
        MainWindow.setMaximumSize(QSize(800, 200))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: white;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.spinner_1 = QFrame(self.centralwidget)
        self.spinner_1.setObjectName(u"spinner_1")
        self.spinner_1.setMinimumSize(QSize(200, 200))
        self.spinner_1.setMaximumSize(QSize(200, 200))
        self.spinner_1.setFrameShape(QFrame.NoFrame)
        self.spinner_1.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.spinner_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.circle_outer_1 = QFrame(self.spinner_1)
        self.circle_outer_1.setObjectName(u"circle_outer_1")
        self.circle_outer_1.setMinimumSize(QSize(170, 170))
        self.circle_outer_1.setMaximumSize(QSize(170, 170))
        self.circle_outer_1.setStyleSheet(u"QFrame{\n"
"border-radius: 85px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.3 #dfdfdf, stop:0.2999 #3F51B5);\n"
"}\n"
"")
        self.circle_outer_1.setFrameShape(QFrame.NoFrame)
        self.circle_outer_1.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.circle_outer_1)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.circle_inner_1 = QFrame(self.circle_outer_1)
        self.circle_inner_1.setObjectName(u"circle_inner_1")
        self.circle_inner_1.setMinimumSize(QSize(150, 150))
        self.circle_inner_1.setMaximumSize(QSize(150, 150))
        self.circle_inner_1.setStyleSheet(u"background: white;\n"
"border-radius: 75px;\n"
"")
        self.circle_inner_1.setFrameShape(QFrame.NoFrame)
        self.circle_inner_1.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.circle_inner_1, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.circle_outer_1, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.spinner_1)

        self.spinner_3 = QFrame(self.centralwidget)
        self.spinner_3.setObjectName(u"spinner_3")
        self.spinner_3.setMinimumSize(QSize(200, 200))
        self.spinner_3.setMaximumSize(QSize(200, 200))
        self.spinner_3.setFrameShape(QFrame.NoFrame)
        self.spinner_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.spinner_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.circle_outer_2 = QFrame(self.spinner_3)
        self.circle_outer_2.setObjectName(u"circle_outer_2")
        self.circle_outer_2.setMinimumSize(QSize(170, 170))
        self.circle_outer_2.setMaximumSize(QSize(170, 170))
        self.circle_outer_2.setStyleSheet(u"border-radius: 85px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.4 #fff, stop:0.3999 #f44336);")
        self.circle_outer_2.setFrameShape(QFrame.StyledPanel)
        self.circle_outer_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.circle_outer_2)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.circle_2_bg_1 = QFrame(self.circle_outer_2)
        self.circle_2_bg_1.setObjectName(u"circle_2_bg_1")
        self.circle_2_bg_1.setMinimumSize(QSize(150, 150))
        self.circle_2_bg_1.setMaximumSize(QSize(150, 150))
        self.circle_2_bg_1.setStyleSheet(u"background: white;\n"
"border-radius: 75px;")
        self.circle_2_bg_1.setFrameShape(QFrame.StyledPanel)
        self.circle_2_bg_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.circle_2_bg_1)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.circle_inner_2 = QFrame(self.circle_2_bg_1)
        self.circle_inner_2.setObjectName(u"circle_inner_2")
        self.circle_inner_2.setMinimumSize(QSize(140, 140))
        self.circle_inner_2.setMaximumSize(QSize(140, 140))
        self.circle_inner_2.setStyleSheet(u"border-radius: 70px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:180, stop:0.4 #fff, stop:0.3999 #f44336);")
        self.circle_inner_2.setFrameShape(QFrame.StyledPanel)
        self.circle_inner_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.circle_inner_2)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.circle_2_bg_2 = QFrame(self.circle_inner_2)
        self.circle_2_bg_2.setObjectName(u"circle_2_bg_2")
        self.circle_2_bg_2.setMinimumSize(QSize(120, 120))
        self.circle_2_bg_2.setMaximumSize(QSize(120, 120))
        self.circle_2_bg_2.setStyleSheet(u"background: white;\n"
"border-radius: 60px;")
        self.circle_2_bg_2.setFrameShape(QFrame.StyledPanel)
        self.circle_2_bg_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.circle_2_bg_2, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.circle_inner_2, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.circle_2_bg_1, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.circle_outer_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.spinner_3)

        self.spinner_4 = QFrame(self.centralwidget)
        self.spinner_4.setObjectName(u"spinner_4")
        self.spinner_4.setMinimumSize(QSize(200, 200))
        self.spinner_4.setMaximumSize(QSize(200, 200))
        self.spinner_4.setFrameShape(QFrame.NoFrame)
        self.spinner_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.spinner_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.circle_outer_3 = QFrame(self.spinner_4)
        self.circle_outer_3.setObjectName(u"circle_outer_3")
        self.circle_outer_3.setMinimumSize(QSize(170, 170))
        self.circle_outer_3.setMaximumSize(QSize(170, 170))
        self.circle_outer_3.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 #689F38, stop:0.454545 #8BC34A, stop:0.784091 #C5E1A5, stop:0.886364 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 85px;\n"
"")
        self.circle_outer_3.setFrameShape(QFrame.NoFrame)
        self.circle_outer_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_10 = QGridLayout(self.circle_outer_3)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.circle_inner_3 = QFrame(self.circle_outer_3)
        self.circle_inner_3.setObjectName(u"circle_inner_3")
        self.circle_inner_3.setMinimumSize(QSize(150, 150))
        self.circle_inner_3.setMaximumSize(QSize(150, 150))
        self.circle_inner_3.setStyleSheet(u"background: white;\n"
"border-radius: 75px;")
        self.circle_inner_3.setFrameShape(QFrame.StyledPanel)
        self.circle_inner_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_10.addWidget(self.circle_inner_3, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.circle_outer_3, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.spinner_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

