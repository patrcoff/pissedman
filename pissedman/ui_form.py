# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QTextBrowser, QTextEdit,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.responseArea = QScrollArea(Widget)
        self.responseArea.setObjectName(u"responseArea")
        self.responseArea.setGeometry(QRect(20, 300, 631, 271))
        self.responseArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 629, 269))
        self.responseViewer = QTextBrowser(self.scrollAreaWidgetContents)
        self.responseViewer.setObjectName(u"responseViewer")
        self.responseViewer.setGeometry(QRect(0, 0, 631, 271))
        self.responseArea.setWidget(self.scrollAreaWidgetContents)
        self.requestArea = QScrollArea(Widget)
        self.requestArea.setObjectName(u"requestArea")
        self.requestArea.setGeometry(QRect(20, 109, 631, 181))
        font = QFont()
        font.setFamilies([u"Noteworthy"])
        self.requestArea.setFont(font)
        self.requestArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 629, 179))
        self.requestEdit = QTextEdit(self.scrollAreaWidgetContents_2)
        self.requestEdit.setObjectName(u"requestEdit")
        self.requestEdit.setGeometry(QRect(0, 0, 631, 181))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        self.requestEdit.setFont(font1)
        self.requestArea.setWidget(self.scrollAreaWidgetContents_2)
        self.sendBtn = QPushButton(Widget)
        self.sendBtn.setObjectName(u"sendBtn")
        self.sendBtn.setGeometry(QRect(670, 52, 100, 40))
        font2 = QFont()
        font2.setFamilies([u"Phosphate"])
        self.sendBtn.setFont(font2)
        self.uriEdit = QLineEdit(Widget)
        self.uriEdit.setObjectName(u"uriEdit")
        self.uriEdit.setGeometry(QRect(60, 60, 591, 31))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(24, 67, 58, 16))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.sendBtn.setText(QCoreApplication.translate("Widget", u"Send", None))
        self.label.setText(QCoreApplication.translate("Widget", u"URI:", None))
    # retranslateUi

