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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 2, 1, 2)

        self.responseViewer = QTextBrowser(Widget)
        self.responseViewer.setObjectName(u"responseViewer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.responseViewer.sizePolicy().hasHeightForWidth())
        self.responseViewer.setSizePolicy(sizePolicy1)
        self.responseViewer.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.responseViewer, 6, 2, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.uriEdit = QLineEdit(Widget)
        self.uriEdit.setObjectName(u"uriEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.uriEdit.sizePolicy().hasHeightForWidth())
        self.uriEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.uriEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.methodCombo = QComboBox(Widget)
        self.methodCombo.addItem("")
        self.methodCombo.addItem("")
        self.methodCombo.addItem("")
        self.methodCombo.addItem("")
        self.methodCombo.addItem("")
        self.methodCombo.setObjectName(u"methodCombo")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(5)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.methodCombo.sizePolicy().hasHeightForWidth())
        self.methodCombo.setSizePolicy(sizePolicy3)
        self.methodCombo.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.horizontalLayout_3.addWidget(self.methodCombo)

        self.pPrint = QCheckBox(Widget)
        self.pPrint.setObjectName(u"pPrint")
        self.pPrint.setChecked(True)

        self.horizontalLayout_3.addWidget(self.pPrint)

        self.appjson = QCheckBox(Widget)
        self.appjson.setObjectName(u"appjson")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(5)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.appjson.sizePolicy().hasHeightForWidth())
        self.appjson.setSizePolicy(sizePolicy4)
        self.appjson.setChecked(True)

        self.horizontalLayout_3.addWidget(self.appjson)

        self.verifySsl = QCheckBox(Widget)
        self.verifySsl.setObjectName(u"verifySsl")
        self.verifySsl.setChecked(True)

        self.horizontalLayout_3.addWidget(self.verifySsl)

        self.allowHttp = QCheckBox(Widget)
        self.allowHttp.setObjectName(u"allowHttp")

        self.horizontalLayout_3.addWidget(self.allowHttp)

        self.params = QCheckBox(Widget)
        self.params.setObjectName(u"params")

        self.horizontalLayout_3.addWidget(self.params)

        self.sendBtn = QPushButton(Widget)
        self.sendBtn.setObjectName(u"sendBtn")
        font = QFont()
        font.setFamilies([u"Phosphate"])
        self.sendBtn.setFont(font)

        self.horizontalLayout_3.addWidget(self.sendBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 5)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)

        self.requestEdit = QPlainTextEdit(Widget)
        self.requestEdit.setObjectName(u"requestEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(100)
        sizePolicy5.setVerticalStretch(10)
        sizePolicy5.setHeightForWidth(self.requestEdit.sizePolicy().hasHeightForWidth())
        self.requestEdit.setSizePolicy(sizePolicy5)
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        self.requestEdit.setFont(font1)
        self.requestEdit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.requestEdit.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.requestEdit, 2, 2, 1, 1)

        self.paramsEdit = QTextEdit(Widget)
        self.paramsEdit.setObjectName(u"paramsEdit")
        sizePolicy5.setHeightForWidth(self.paramsEdit.sizePolicy().hasHeightForWidth())
        self.paramsEdit.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.paramsEdit, 2, 3, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"URI:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Method:", None))
        self.methodCombo.setItemText(0, QCoreApplication.translate("Widget", u"GET", None))
        self.methodCombo.setItemText(1, QCoreApplication.translate("Widget", u"PUT", None))
        self.methodCombo.setItemText(2, QCoreApplication.translate("Widget", u"POST", None))
        self.methodCombo.setItemText(3, QCoreApplication.translate("Widget", u"DELETE", None))
        self.methodCombo.setItemText(4, QCoreApplication.translate("Widget", u"OPTIONS", None))

        self.pPrint.setText(QCoreApplication.translate("Widget", u"PPrint", None))
        self.appjson.setText(QCoreApplication.translate("Widget", u"APPLICATION/JSON", None))
        self.verifySsl.setText(QCoreApplication.translate("Widget", u"Verify SSL", None))
        self.allowHttp.setText(QCoreApplication.translate("Widget", u"Allow HTTP", None))
        self.params.setText(QCoreApplication.translate("Widget", u"Params", None))
        self.sendBtn.setText(QCoreApplication.translate("Widget", u"Send", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Request Body", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Query Parameters (JSON syntax)", None))
    # retranslateUi

