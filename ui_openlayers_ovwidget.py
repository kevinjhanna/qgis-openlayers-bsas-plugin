# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_openlayers_ovwidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(457, 467)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lytEnableMap = QtGui.QHBoxLayout()
        self.lytEnableMap.setObjectName(_fromUtf8("lytEnableMap"))
        self.checkBoxEnableMap = QtGui.QCheckBox(Form)
        self.checkBoxEnableMap.setChecked(False)
        self.checkBoxEnableMap.setObjectName(_fromUtf8("checkBoxEnableMap"))
        self.lytEnableMap.addWidget(self.checkBoxEnableMap)
        self.comboBoxTypeMap = QtGui.QComboBox(Form)
        self.comboBoxTypeMap.setObjectName(_fromUtf8("comboBoxTypeMap"))
        self.lytEnableMap.addWidget(self.comboBoxTypeMap)
        self.pbAddRaster = QtGui.QPushButton(Form)
        self.pbAddRaster.setText(_fromUtf8(""))
        self.pbAddRaster.setObjectName(_fromUtf8("pbAddRaster"))
        self.lytEnableMap.addWidget(self.pbAddRaster)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lytEnableMap.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.lytEnableMap)
        self.lbStatusRead = QtGui.QLabel(Form)
        self.lbStatusRead.setText(_fromUtf8(""))
        self.lbStatusRead.setTextFormat(QtCore.Qt.PlainText)
        self.lbStatusRead.setObjectName(_fromUtf8("lbStatusRead"))
        self.verticalLayout_2.addWidget(self.lbStatusRead)
        self.webViewMap = QtWebKit.QWebView(Form)
        self.webViewMap.setObjectName(_fromUtf8("webViewMap"))
        self.verticalLayout_2.addWidget(self.webViewMap)
        self.lytHideCross = QtGui.QHBoxLayout()
        self.lytHideCross.setObjectName(_fromUtf8("lytHideCross"))
        self.checkBoxHideCross = QtGui.QCheckBox(Form)
        self.checkBoxHideCross.setObjectName(_fromUtf8("checkBoxHideCross"))
        self.lytHideCross.addWidget(self.checkBoxHideCross)
        self.pbRefresh = QtGui.QPushButton(Form)
        self.pbRefresh.setText(_fromUtf8(""))
        self.pbRefresh.setObjectName(_fromUtf8("pbRefresh"))
        self.lytHideCross.addWidget(self.pbRefresh)
        self.pbSaveImg = QtGui.QPushButton(Form)
        self.pbSaveImg.setText(_fromUtf8(""))
        self.pbSaveImg.setObjectName(_fromUtf8("pbSaveImg"))
        self.lytHideCross.addWidget(self.pbSaveImg)
        self.pbCopyKml = QtGui.QPushButton(Form)
        self.pbCopyKml.setText(_fromUtf8(""))
        self.pbCopyKml.setObjectName(_fromUtf8("pbCopyKml"))
        self.lytHideCross.addWidget(self.pbCopyKml)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lytHideCross.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.lytHideCross)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.checkBoxEnableMap.setText(_translate("Form", "Enable map", None))
        self.pbAddRaster.setToolTip(_translate("Form", "Add map", None))
        self.checkBoxHideCross.setText(_translate("Form", "Hide cross in map", None))
        self.pbRefresh.setToolTip(_translate("Form", "Refresh map", None))
        self.pbSaveImg.setToolTip(_translate("Form", "Save this image", None))
        self.pbCopyKml.setToolTip(_translate("Form", "Copy rectangle (KML) of map to clipboard", None))

from PyQt4 import QtWebKit
