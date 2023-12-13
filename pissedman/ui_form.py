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
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.uriEdit = QLineEdit(Widget)
        self.uriEdit.setObjectName(u"uriEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.uriEdit.sizePolicy().hasHeightForWidth())
        self.uriEdit.setSizePolicy(sizePolicy1)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.methodCombo.sizePolicy().hasHeightForWidth())
        self.methodCombo.setSizePolicy(sizePolicy2)
        self.methodCombo.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.horizontalLayout_3.addWidget(self.methodCombo)

        self.checkBox_4 = QCheckBox(Widget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_4)

        self.checkBox_6 = QCheckBox(Widget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(5)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy3)
        self.checkBox_6.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_6)

        self.checkBox = QCheckBox(Widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(Widget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_3.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(Widget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_3.addWidget(self.checkBox_3)

        self.sendBtn = QPushButton(Widget)
        self.sendBtn.setObjectName(u"sendBtn")
        font = QFont()
        font.setFamilies([u"Phosphate"])
        self.sendBtn.setFont(font)

        self.horizontalLayout_3.addWidget(self.sendBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 2, 3)

        self.requestEdit = QPlainTextEdit(Widget)
        self.requestEdit.setObjectName(u"requestEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(100)
        sizePolicy4.setVerticalStretch(10)
        sizePolicy4.setHeightForWidth(self.requestEdit.sizePolicy().hasHeightForWidth())
        self.requestEdit.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        self.requestEdit.setFont(font1)
        self.requestEdit.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.gridLayout.addWidget(self.requestEdit, 2, 1, 1, 1)

        self.paramsEdit = QTextEdit(Widget)
        self.paramsEdit.setObjectName(u"paramsEdit")
        sizePolicy4.setHeightForWidth(self.paramsEdit.sizePolicy().hasHeightForWidth())
        self.paramsEdit.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.paramsEdit, 2, 2, 1, 1)

        self.responseViewer = QTextBrowser(Widget)
        self.responseViewer.setObjectName(u"responseViewer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(100)
        sizePolicy5.setHeightForWidth(self.responseViewer.sizePolicy().hasHeightForWidth())
        self.responseViewer.setSizePolicy(sizePolicy5)
        self.responseViewer.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.responseViewer, 3, 1, 1, 2)


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

        self.checkBox_4.setText(QCoreApplication.translate("Widget", u"PPrint", None))
        self.checkBox_6.setText(QCoreApplication.translate("Widget", u"APPLICATION/JSON", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"Verify SSL", None))
        self.checkBox_2.setText(QCoreApplication.translate("Widget", u"Allow HTTP", None))
        self.checkBox_3.setText(QCoreApplication.translate("Widget", u"Params", None))
        self.sendBtn.setText(QCoreApplication.translate("Widget", u"Send", None))
    # retranslateUi

