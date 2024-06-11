# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 150, 351, 461))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.piechart_view = QChartView(self.page)
        self.piechart_view.setObjectName(u"piechart_view")
        self.piechart_view.setGeometry(QRect(10, 10, 331, 311))
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 330, 331, 129))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.python = QLineEdit(self.widget)
        self.python.setObjectName(u"python")

        self.verticalLayout_6.addWidget(self.python)

        self.javascript = QLineEdit(self.widget)
        self.javascript.setObjectName(u"javascript")

        self.verticalLayout_6.addWidget(self.javascript)

        self.java = QLineEdit(self.widget)
        self.java.setObjectName(u"java")

        self.verticalLayout_6.addWidget(self.java)

        self.csharp = QLineEdit(self.widget)
        self.csharp.setObjectName(u"csharp")

        self.verticalLayout_6.addWidget(self.csharp)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.linegraph_view = QChartView(self.page_2)
        self.linegraph_view.setObjectName(u"linegraph_view")
        self.linegraph_view.setGeometry(QRect(10, 10, 331, 431))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.barchart_view = QChartView(self.page_3)
        self.barchart_view.setObjectName(u"barchart_view")
        self.barchart_view.setGeometry(QRect(10, 10, 331, 441))
        self.stackedWidget.addWidget(self.page_3)
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_5 = QVBoxLayout(self.widget1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 10, 349, 124))
        self.verticalLayout_3 = QVBoxLayout(self.widget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title1 = QLabel(self.widget2)
        self.title1.setObjectName(u"title1")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.title1.setFont(font)

        self.verticalLayout.addWidget(self.title1)

        self.title2 = QLabel(self.widget2)
        self.title2.setObjectName(u"title2")

        self.verticalLayout.addWidget(self.title2)

        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.widget3 = QWidget(self.widget2)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setStyleSheet(u"QWidget{\n"
"	background-color: #eff;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: blue;\n"
"	color: white;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.piechart_btn = QPushButton(self.widget3)
        self.piechart_btn.setObjectName(u"piechart_btn")
        icon = QIcon()
        icon.addFile(u"icons/icons8-piechart-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.piechart_btn.setIcon(icon)
        self.piechart_btn.setCheckable(True)
        self.piechart_btn.setChecked(True)
        self.piechart_btn.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.piechart_btn)

        self.linegraph_btn = QPushButton(self.widget3)
        self.linegraph_btn.setObjectName(u"linegraph_btn")
        icon1 = QIcon()
        icon1.addFile(u"icons/icons8-bar-chart-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.linegraph_btn.setIcon(icon1)
        self.linegraph_btn.setCheckable(True)
        self.linegraph_btn.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.linegraph_btn)

        self.barchart_btn = QPushButton(self.widget3)
        self.barchart_btn.setObjectName(u"barchart_btn")
        self.barchart_btn.setIcon(icon1)
        self.barchart_btn.setCheckable(True)
        self.barchart_btn.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.barchart_btn)


        self.verticalLayout_2.addWidget(self.widget3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Python", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Javascript", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Java", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"C#", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Update Chart", None))
        self.title1.setText(QCoreApplication.translate("MainWindow", u"Most popular programming languages", None))
        self.title2.setText(QCoreApplication.translate("MainWindow", u"some most commonly recognized programming languages that appear", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"in lots of top languages include:", None))
        self.piechart_btn.setText(QCoreApplication.translate("MainWindow", u"Pie Chart", None))
        self.linegraph_btn.setText(QCoreApplication.translate("MainWindow", u"Line Graph", None))
        self.barchart_btn.setText(QCoreApplication.translate("MainWindow", u"Bar Chart", None))
    # retranslateUi

