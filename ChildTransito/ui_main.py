# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janelagrafica.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(533, 585)
        MainWindow.setMinimumSize(QSize(300, 31))
        MainWindow.setMaximumSize(QSize(16777215, 593))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: #FFE9A0")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_2 = QVBoxLayout(self.pg_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_logo = QLabel(self.pg_home)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setStyleSheet(u"back ground-color: #FFE9A0")

        self.verticalLayout_2.addWidget(self.lbl_logo)

        self.btn_inicio = QPushButton(self.pg_home)
        self.btn_inicio.setObjectName(u"btn_inicio")
        self.btn_inicio.setMinimumSize(QSize(300, 31))
        self.btn_inicio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inicio.setStyleSheet(u"QPushButton{\n"
"	background-color:#367E18;\n"
"	color: rgb(255,255,255);\n"
"	border-color: rgb(255,255,255);\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #ffff;\n"
"	background-color: rgb(74, 146, 30)\n"
"\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_inicio)

        self.Pages.addWidget(self.pg_home)
        self.pg_inicio = QWidget()
        self.pg_inicio.setObjectName(u"pg_inicio")
        self.verticalLayout_3 = QVBoxLayout(self.pg_inicio)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.pg_inicio)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_2)

        self.frame = QFrame(self.pg_inicio)
        self.frame.setObjectName(u"frame")
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setStyleSheet(u"QPushButton{\n"
"	background-color:#367E18;\n"
"	color: rgb(255,255,255);\n"
"	border-color: rgb(255,255,255);\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #ffff;\n"
"	background-color: rgb(74, 146, 30)\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_play = QPushButton(self.frame)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMinimumSize(QSize(150, 31))
        self.btn_play.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_play)

        self.btn_exit = QPushButton(self.frame)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(150, 31))
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_exit)


        self.verticalLayout_3.addWidget(self.frame)

        self.Pages.addWidget(self.pg_inicio)
        self.pg_game = QWidget()
        self.pg_game.setObjectName(u"pg_game")
        self.horizontalLayout_2 = QHBoxLayout(self.pg_game)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.pg_game)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 250, 481, 231))
        self.frame_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_3.setStyleSheet(u"QCommandLinkButton{\n"
"background-color: #FFA41B;\n"
"border-radius: 15px;\n"
"border: 2px solid white;\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"QCommandLinkButton:hover{\n"
"	background-color: rgb(255,174, 47);\n"
"	border-radius:15px;\n"
"	border:2px solid white;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_resp_1 = QCommandLinkButton(self.frame_3)
        self.btn_resp_1.setObjectName(u"btn_resp_1")
        self.btn_resp_1.setMaximumSize(QSize(16777215, 40))
        self.btn_resp_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/87e4e52fb818c32689d0e717a36b92d1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_resp_1.setIcon(icon)

        self.verticalLayout_4.addWidget(self.btn_resp_1)

        self.btn_resp_2 = QCommandLinkButton(self.frame_3)
        self.btn_resp_2.setObjectName(u"btn_resp_2")
        self.btn_resp_2.setMaximumSize(QSize(16777215, 40))
        self.btn_resp_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_resp_2.setIcon(icon)

        self.verticalLayout_4.addWidget(self.btn_resp_2)

        self.btn_resp_3 = QCommandLinkButton(self.frame_3)
        self.btn_resp_3.setObjectName(u"btn_resp_3")
        self.btn_resp_3.setMaximumSize(QSize(16777215, 40))
        self.btn_resp_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_resp_3.setIcon(icon)

        self.verticalLayout_4.addWidget(self.btn_resp_3)

        self.btn_resp_4 = QCommandLinkButton(self.frame_3)
        self.btn_resp_4.setObjectName(u"btn_resp_4")
        self.btn_resp_4.setMaximumSize(QSize(16777215, 40))
        self.btn_resp_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_resp_4.setIcon(icon)

        self.verticalLayout_4.addWidget(self.btn_resp_4)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 481, 181))
        self.label_3.setStyleSheet(u"background-color: #FFA41B;\n"
"border-radius: 15px;\n"
"border: 2px solid white;\n"
"color: rgb(255, 255, 255)")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 481, 31))
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 490, 481, 71))
        self.frame_4.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_stop = QPushButton(self.frame_4)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMinimumSize(QSize(150, 31))
        self.btn_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop.setStyleSheet(u"QPushButton{\n"
"	background-color:#CC3636;\n"
"	color: rgb(255,255,255);\n"
"	border-color: rgb(255,255,255);\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #ffff;\n"
"	background-color: rgb(215, 70, 70)\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_stop)

        self.btn_verification = QPushButton(self.frame_4)
        self.btn_verification.setObjectName(u"btn_verification")
        self.btn_verification.setMinimumSize(QSize(150, 31))
        self.btn_verification.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_verification.setStyleSheet(u"QPushButton{\n"
"	background-color:#367E18;\n"
"	color: rgb(255,255,255);\n"
"	border-color: rgb(255,255,255);\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #ffff;\n"
"	background-color: rgb(74, 146, 30)\n"
"\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_verification)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.Pages.addWidget(self.pg_game)

        self.verticalLayout.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/Untitled design.png\"/></p></body></html>", None))
        self.btn_inicio.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/Untitled design.png\"/></p></body></html>", None))
        self.btn_play.setText(QCoreApplication.translate("MainWindow", u"Jogar", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.btn_resp_1.setText("")
        self.btn_resp_2.setText("")
        self.btn_resp_3.setText("")
        self.btn_resp_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Quest\u00f5es:", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"Parar Jogo", None))
        self.btn_verification.setText(QCoreApplication.translate("MainWindow", u"Verificar Resposta", None))
    # retranslateUi

