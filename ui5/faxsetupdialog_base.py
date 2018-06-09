# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui5/faxsetupdialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        self.gridlayout = QtWidgets.QGridLayout(Dialog)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridlayout.addWidget(self.line, 1, 0, 1, 3)
        self.FaxComboBox = DeviceUriComboBox(Dialog)
        self.FaxComboBox.setObjectName("FaxComboBox")
        self.gridlayout.addWidget(self.FaxComboBox, 2, 0, 1, 3)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridlayout1 = QtWidgets.QGridLayout(self.tab)
        self.gridlayout1.setObjectName("gridlayout1")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridlayout1.addWidget(self.label_3, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridlayout1.addWidget(self.label_2, 1, 0, 1, 1)
        self.NameCompanyLineEdit = QtWidgets.QLineEdit(self.tab)
        self.NameCompanyLineEdit.setObjectName("NameCompanyLineEdit")
        self.gridlayout1.addWidget(self.NameCompanyLineEdit, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridlayout1.addWidget(self.label_4, 2, 0, 1, 1)
        self.FaxNumberLineEdit = QtWidgets.QLineEdit(self.tab)
        self.FaxNumberLineEdit.setObjectName("FaxNumberLineEdit")
        self.gridlayout1.addWidget(self.FaxNumberLineEdit, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridlayout2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridlayout2.setObjectName("gridlayout2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridlayout2.addWidget(self.label_5, 0, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridlayout2.addWidget(self.label_6, 1, 0, 1, 1)
        self.VoiceNumberLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.VoiceNumberLineEdit.setObjectName("VoiceNumberLineEdit")
        self.gridlayout2.addWidget(self.VoiceNumberLineEdit, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridlayout2.addWidget(self.label_7, 2, 0, 1, 1)
        self.EmailLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.EmailLineEdit.setObjectName("EmailLineEdit")
        self.gridlayout2.addWidget(self.EmailLineEdit, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 131, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout2.addItem(spacerItem1, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridlayout.addWidget(self.tabWidget, 3, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(371, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.CancelButton = QtWidgets.QPushButton(Dialog)
        self.CancelButton.setObjectName("CancelButton")
        self.gridlayout.addWidget(self.CancelButton, 4, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HP Device Manager - Fax Device Setup"))
        self.label.setText(_translate("Dialog", "Fax Device Setup"))
        self.label_3.setText(_translate("Dialog", "This information will appear at the top of each fax you send."))
        self.label_2.setText(_translate("Dialog", "Name and/or Company:"))
        self.label_4.setText(_translate("Dialog", "Fax Number:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Fax Header"))
        self.label_5.setText(_translate("Dialog", "This information will appear on all coverpages."))
        self.label_6.setText(_translate("Dialog", "Voice Phone Number:"))
        self.label_7.setText(_translate("Dialog", "Email Address:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Coverpage"))
        self.CancelButton.setText(_translate("Dialog", "Close"))

from .deviceuricombobox import DeviceUriComboBox
