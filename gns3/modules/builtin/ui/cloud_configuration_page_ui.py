# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/workspace/git/gns3-gui/gns3/modules/dynamips/ui/cloud_configuration_page.ui'
#
# Created: Mon Mar 17 17:42:16 2014
#      by: PyQt4 UI code generator 4.10
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


class Ui_cloudConfigPageWidget(object):

    def setupUi(self, cloudConfigPageWidget):
        cloudConfigPageWidget.setObjectName(_fromUtf8("cloudConfigPageWidget"))
        cloudConfigPageWidget.resize(542, 500)
        self.vboxlayout = QtGui.QVBoxLayout(cloudConfigPageWidget)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.tabWidget = QtGui.QTabWidget(cloudConfigPageWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.uiGenericEthernetGroupBox = QtGui.QGroupBox(self.tab)
        self.uiGenericEthernetGroupBox.setObjectName(_fromUtf8("uiGenericEthernetGroupBox"))
        self.gridlayout = QtGui.QGridLayout(self.uiGenericEthernetGroupBox)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.uiGenericEthernetComboBox = QtGui.QComboBox(self.uiGenericEthernetGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiGenericEthernetComboBox.sizePolicy().hasHeightForWidth())
        self.uiGenericEthernetComboBox.setSizePolicy(sizePolicy)
        self.uiGenericEthernetComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.uiGenericEthernetComboBox.setObjectName(_fromUtf8("uiGenericEthernetComboBox"))
        self.gridlayout.addWidget(self.uiGenericEthernetComboBox, 0, 0, 1, 3)
        self.uiGenericEthernetLineEdit = QtGui.QLineEdit(self.uiGenericEthernetGroupBox)
        self.uiGenericEthernetLineEdit.setObjectName(_fromUtf8("uiGenericEthernetLineEdit"))
        self.gridlayout.addWidget(self.uiGenericEthernetLineEdit, 1, 0, 1, 1)
        self.uiAddGenericEthernetPushButton = QtGui.QPushButton(self.uiGenericEthernetGroupBox)
        self.uiAddGenericEthernetPushButton.setObjectName(_fromUtf8("uiAddGenericEthernetPushButton"))
        self.gridlayout.addWidget(self.uiAddGenericEthernetPushButton, 1, 1, 1, 1)
        self.uiDeleteGenericEthernetPushButton = QtGui.QPushButton(self.uiGenericEthernetGroupBox)
        self.uiDeleteGenericEthernetPushButton.setEnabled(False)
        self.uiDeleteGenericEthernetPushButton.setObjectName(_fromUtf8("uiDeleteGenericEthernetPushButton"))
        self.gridlayout.addWidget(self.uiDeleteGenericEthernetPushButton, 1, 2, 1, 1)
        self.uiGenericEthernetListWidget = QtGui.QListWidget(self.uiGenericEthernetGroupBox)
        self.uiGenericEthernetListWidget.setObjectName(_fromUtf8("uiGenericEthernetListWidget"))
        self.gridlayout.addWidget(self.uiGenericEthernetListWidget, 2, 0, 1, 3)
        self.vboxlayout1.addWidget(self.uiGenericEthernetGroupBox)
        self.uiLinuxEthernetGroupBox = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLinuxEthernetGroupBox.sizePolicy().hasHeightForWidth())
        self.uiLinuxEthernetGroupBox.setSizePolicy(sizePolicy)
        self.uiLinuxEthernetGroupBox.setObjectName(_fromUtf8("uiLinuxEthernetGroupBox"))
        self.gridlayout1 = QtGui.QGridLayout(self.uiLinuxEthernetGroupBox)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.uiLinuxEthernetComboBox = QtGui.QComboBox(self.uiLinuxEthernetGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLinuxEthernetComboBox.sizePolicy().hasHeightForWidth())
        self.uiLinuxEthernetComboBox.setSizePolicy(sizePolicy)
        self.uiLinuxEthernetComboBox.setObjectName(_fromUtf8("uiLinuxEthernetComboBox"))
        self.gridlayout1.addWidget(self.uiLinuxEthernetComboBox, 0, 0, 1, 3)
        self.uiLinuxEthernetLineEdit = QtGui.QLineEdit(self.uiLinuxEthernetGroupBox)
        self.uiLinuxEthernetLineEdit.setObjectName(_fromUtf8("uiLinuxEthernetLineEdit"))
        self.gridlayout1.addWidget(self.uiLinuxEthernetLineEdit, 1, 0, 1, 1)
        self.uiAddLinuxEthernetPushButton = QtGui.QPushButton(self.uiLinuxEthernetGroupBox)
        self.uiAddLinuxEthernetPushButton.setObjectName(_fromUtf8("uiAddLinuxEthernetPushButton"))
        self.gridlayout1.addWidget(self.uiAddLinuxEthernetPushButton, 1, 1, 1, 1)
        self.uiDeleteLinuxEthernetPushButton = QtGui.QPushButton(self.uiLinuxEthernetGroupBox)
        self.uiDeleteLinuxEthernetPushButton.setEnabled(False)
        self.uiDeleteLinuxEthernetPushButton.setObjectName(_fromUtf8("uiDeleteLinuxEthernetPushButton"))
        self.gridlayout1.addWidget(self.uiDeleteLinuxEthernetPushButton, 1, 2, 1, 1)
        self.uiLinuxEthernetListWidget = QtGui.QListWidget(self.uiLinuxEthernetGroupBox)
        self.uiLinuxEthernetListWidget.setObjectName(_fromUtf8("uiLinuxEthernetListWidget"))
        self.gridlayout1.addWidget(self.uiLinuxEthernetListWidget, 2, 0, 1, 3)
        self.vboxlayout1.addWidget(self.uiLinuxEthernetGroupBox)
        spacerItem = QtGui.QSpacerItem(21, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.vboxlayout1.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridlayout2 = QtGui.QGridLayout(self.tab_2)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.uiNIOUDPSettingsGroupBox = QtGui.QGroupBox(self.tab_2)
        self.uiNIOUDPSettingsGroupBox.setObjectName(_fromUtf8("uiNIOUDPSettingsGroupBox"))
        self.gridlayout3 = QtGui.QGridLayout(self.uiNIOUDPSettingsGroupBox)
        self.gridlayout3.setObjectName(_fromUtf8("gridlayout3"))
        self.uiLocalPortLabel = QtGui.QLabel(self.uiNIOUDPSettingsGroupBox)
        self.uiLocalPortLabel.setObjectName(_fromUtf8("uiLocalPortLabel"))
        self.gridlayout3.addWidget(self.uiLocalPortLabel, 0, 0, 1, 1)
        self.uiLocalPortSpinBox = QtGui.QSpinBox(self.uiNIOUDPSettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiLocalPortSpinBox.setSizePolicy(sizePolicy)
        self.uiLocalPortSpinBox.setMaximum(65535)
        self.uiLocalPortSpinBox.setProperty("value", 30000)
        self.uiLocalPortSpinBox.setObjectName(_fromUtf8("uiLocalPortSpinBox"))
        self.gridlayout3.addWidget(self.uiLocalPortSpinBox, 0, 1, 1, 1)
        self.uiRemoteHostLabel = QtGui.QLabel(self.uiNIOUDPSettingsGroupBox)
        self.uiRemoteHostLabel.setObjectName(_fromUtf8("uiRemoteHostLabel"))
        self.gridlayout3.addWidget(self.uiRemoteHostLabel, 1, 0, 1, 1)
        self.uiRemoteHostLineEdit = QtGui.QLineEdit(self.uiNIOUDPSettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteHostLineEdit.sizePolicy().hasHeightForWidth())
        self.uiRemoteHostLineEdit.setSizePolicy(sizePolicy)
        self.uiRemoteHostLineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.uiRemoteHostLineEdit.setObjectName(_fromUtf8("uiRemoteHostLineEdit"))
        self.gridlayout3.addWidget(self.uiRemoteHostLineEdit, 1, 1, 1, 1)
        self.uiRemotePortLabel = QtGui.QLabel(self.uiNIOUDPSettingsGroupBox)
        self.uiRemotePortLabel.setObjectName(_fromUtf8("uiRemotePortLabel"))
        self.gridlayout3.addWidget(self.uiRemotePortLabel, 2, 0, 1, 1)
        self.uiRemotePortSpinBox = QtGui.QSpinBox(self.uiNIOUDPSettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemotePortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRemotePortSpinBox.setSizePolicy(sizePolicy)
        self.uiRemotePortSpinBox.setMaximum(65535)
        self.uiRemotePortSpinBox.setProperty("value", 20000)
        self.uiRemotePortSpinBox.setObjectName(_fromUtf8("uiRemotePortSpinBox"))
        self.gridlayout3.addWidget(self.uiRemotePortSpinBox, 2, 1, 1, 1)
        self.gridlayout2.addWidget(self.uiNIOUDPSettingsGroupBox, 0, 0, 1, 2)
        self.uiNIOUDPListGroupBox = QtGui.QGroupBox(self.tab_2)
        self.uiNIOUDPListGroupBox.setObjectName(_fromUtf8("uiNIOUDPListGroupBox"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.uiNIOUDPListGroupBox)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.uiNIOUDPListWidget = QtGui.QListWidget(self.uiNIOUDPListGroupBox)
        self.uiNIOUDPListWidget.setObjectName(_fromUtf8("uiNIOUDPListWidget"))
        self.vboxlayout2.addWidget(self.uiNIOUDPListWidget)
        self.gridlayout2.addWidget(self.uiNIOUDPListGroupBox, 0, 2, 2, 1)
        self.uiAddNIOUDPPushButton = QtGui.QPushButton(self.tab_2)
        self.uiAddNIOUDPPushButton.setObjectName(_fromUtf8("uiAddNIOUDPPushButton"))
        self.gridlayout2.addWidget(self.uiAddNIOUDPPushButton, 1, 0, 1, 1)
        self.uiDeleteNIOUDPPushButton = QtGui.QPushButton(self.tab_2)
        self.uiDeleteNIOUDPPushButton.setEnabled(False)
        self.uiDeleteNIOUDPPushButton.setObjectName(_fromUtf8("uiDeleteNIOUDPPushButton"))
        self.gridlayout2.addWidget(self.uiDeleteNIOUDPPushButton, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 211, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout2.addItem(spacerItem1, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.vboxlayout3 = QtGui.QVBoxLayout(self.tab_3)
        self.vboxlayout3.setObjectName(_fromUtf8("vboxlayout3"))
        self.uiNIOTAPGroupBox = QtGui.QGroupBox(self.tab_3)
        self.uiNIOTAPGroupBox.setObjectName(_fromUtf8("uiNIOTAPGroupBox"))
        self.gridlayout4 = QtGui.QGridLayout(self.uiNIOTAPGroupBox)
        self.gridlayout4.setObjectName(_fromUtf8("gridlayout4"))
        self.uiNIOTAPLineEdit = QtGui.QLineEdit(self.uiNIOTAPGroupBox)
        self.uiNIOTAPLineEdit.setObjectName(_fromUtf8("uiNIOTAPLineEdit"))
        self.gridlayout4.addWidget(self.uiNIOTAPLineEdit, 0, 0, 1, 1)
        self.uiAddNIOTAPPushButton = QtGui.QPushButton(self.uiNIOTAPGroupBox)
        self.uiAddNIOTAPPushButton.setObjectName(_fromUtf8("uiAddNIOTAPPushButton"))
        self.gridlayout4.addWidget(self.uiAddNIOTAPPushButton, 0, 1, 1, 1)
        self.uiDeleteNIOTAPPushButton = QtGui.QPushButton(self.uiNIOTAPGroupBox)
        self.uiDeleteNIOTAPPushButton.setEnabled(False)
        self.uiDeleteNIOTAPPushButton.setObjectName(_fromUtf8("uiDeleteNIOTAPPushButton"))
        self.gridlayout4.addWidget(self.uiDeleteNIOTAPPushButton, 0, 2, 1, 1)
        self.uiNIOTAPListWidget = QtGui.QListWidget(self.uiNIOTAPGroupBox)
        self.uiNIOTAPListWidget.setObjectName(_fromUtf8("uiNIOTAPListWidget"))
        self.gridlayout4.addWidget(self.uiNIOTAPListWidget, 1, 0, 1, 3)
        self.vboxlayout3.addWidget(self.uiNIOTAPGroupBox)
        spacerItem2 = QtGui.QSpacerItem(20, 191, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridlayout5 = QtGui.QGridLayout(self.tab_4)
        self.gridlayout5.setObjectName(_fromUtf8("gridlayout5"))
        self.uiNIOUNIXSettingsGroupBox = QtGui.QGroupBox(self.tab_4)
        self.uiNIOUNIXSettingsGroupBox.setObjectName(_fromUtf8("uiNIOUNIXSettingsGroupBox"))
        self.gridlayout6 = QtGui.QGridLayout(self.uiNIOUNIXSettingsGroupBox)
        self.gridlayout6.setObjectName(_fromUtf8("gridlayout6"))
        self.gridlayout7 = QtGui.QGridLayout()
        self.gridlayout7.setObjectName(_fromUtf8("gridlayout7"))
        self.uiLocalFileLabel = QtGui.QLabel(self.uiNIOUNIXSettingsGroupBox)
        self.uiLocalFileLabel.setObjectName(_fromUtf8("uiLocalFileLabel"))
        self.gridlayout7.addWidget(self.uiLocalFileLabel, 0, 0, 1, 1)
        self.uiLocalFileLineEdit = QtGui.QLineEdit(self.uiNIOUNIXSettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalFileLineEdit.sizePolicy().hasHeightForWidth())
        self.uiLocalFileLineEdit.setSizePolicy(sizePolicy)
        self.uiLocalFileLineEdit.setObjectName(_fromUtf8("uiLocalFileLineEdit"))
        self.gridlayout7.addWidget(self.uiLocalFileLineEdit, 1, 0, 1, 1)
        self.gridlayout6.addLayout(self.gridlayout7, 0, 0, 1, 1)
        self.gridlayout8 = QtGui.QGridLayout()
        self.gridlayout8.setObjectName(_fromUtf8("gridlayout8"))
        self.uiRemoteFileLabel = QtGui.QLabel(self.uiNIOUNIXSettingsGroupBox)
        self.uiRemoteFileLabel.setObjectName(_fromUtf8("uiRemoteFileLabel"))
        self.gridlayout8.addWidget(self.uiRemoteFileLabel, 0, 0, 1, 1)
        self.uiRemoteFileLineEdit = QtGui.QLineEdit(self.uiNIOUNIXSettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteFileLineEdit.sizePolicy().hasHeightForWidth())
        self.uiRemoteFileLineEdit.setSizePolicy(sizePolicy)
        self.uiRemoteFileLineEdit.setObjectName(_fromUtf8("uiRemoteFileLineEdit"))
        self.gridlayout8.addWidget(self.uiRemoteFileLineEdit, 1, 0, 1, 1)
        self.gridlayout6.addLayout(self.gridlayout8, 1, 0, 1, 1)
        self.gridlayout5.addWidget(self.uiNIOUNIXSettingsGroupBox, 0, 0, 1, 2)
        self.uiNIOUNIXListGroupBox = QtGui.QGroupBox(self.tab_4)
        self.uiNIOUNIXListGroupBox.setObjectName(_fromUtf8("uiNIOUNIXListGroupBox"))
        self.vboxlayout4 = QtGui.QVBoxLayout(self.uiNIOUNIXListGroupBox)
        self.vboxlayout4.setObjectName(_fromUtf8("vboxlayout4"))
        self.uiNIOUNIXListWidget = QtGui.QListWidget(self.uiNIOUNIXListGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNIOUNIXListWidget.sizePolicy().hasHeightForWidth())
        self.uiNIOUNIXListWidget.setSizePolicy(sizePolicy)
        self.uiNIOUNIXListWidget.setObjectName(_fromUtf8("uiNIOUNIXListWidget"))
        self.vboxlayout4.addWidget(self.uiNIOUNIXListWidget)
        self.gridlayout5.addWidget(self.uiNIOUNIXListGroupBox, 0, 2, 3, 1)
        self.uiAddNIOUNIXPushButton = QtGui.QPushButton(self.tab_4)
        self.uiAddNIOUNIXPushButton.setObjectName(_fromUtf8("uiAddNIOUNIXPushButton"))
        self.gridlayout5.addWidget(self.uiAddNIOUNIXPushButton, 1, 0, 1, 1)
        self.uiDeleteNIOUNIXPushButton = QtGui.QPushButton(self.tab_4)
        self.uiDeleteNIOUNIXPushButton.setEnabled(False)
        self.uiDeleteNIOUNIXPushButton.setObjectName(_fromUtf8("uiDeleteNIOUNIXPushButton"))
        self.gridlayout5.addWidget(self.uiDeleteNIOUNIXPushButton, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(160, 190, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridlayout5.addItem(spacerItem3, 2, 0, 2, 2)
        spacerItem4 = QtGui.QSpacerItem(196, 132, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout5.addItem(spacerItem4, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridlayout9 = QtGui.QGridLayout(self.tab_5)
        self.gridlayout9.setObjectName(_fromUtf8("gridlayout9"))
        self.uiNIOVDESettingsGroupBox = QtGui.QGroupBox(self.tab_5)
        self.uiNIOVDESettingsGroupBox.setObjectName(_fromUtf8("uiNIOVDESettingsGroupBox"))
        self.gridlayout10 = QtGui.QGridLayout(self.uiNIOVDESettingsGroupBox)
        self.gridlayout10.setObjectName(_fromUtf8("gridlayout10"))
        self.gridlayout11 = QtGui.QGridLayout()
        self.gridlayout11.setObjectName(_fromUtf8("gridlayout11"))
        self.uiVDEControlFileLabel = QtGui.QLabel(self.uiNIOVDESettingsGroupBox)
        self.uiVDEControlFileLabel.setObjectName(_fromUtf8("uiVDEControlFileLabel"))
        self.gridlayout11.addWidget(self.uiVDEControlFileLabel, 0, 0, 1, 1)
        self.uiVDEControlFileLineEdit = QtGui.QLineEdit(self.uiNIOVDESettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVDEControlFileLineEdit.sizePolicy().hasHeightForWidth())
        self.uiVDEControlFileLineEdit.setSizePolicy(sizePolicy)
        self.uiVDEControlFileLineEdit.setObjectName(_fromUtf8("uiVDEControlFileLineEdit"))
        self.gridlayout11.addWidget(self.uiVDEControlFileLineEdit, 1, 0, 1, 1)
        self.gridlayout10.addLayout(self.gridlayout11, 0, 0, 1, 1)
        self.gridlayout12 = QtGui.QGridLayout()
        self.gridlayout12.setObjectName(_fromUtf8("gridlayout12"))
        self.uiVDELocalFileLabel = QtGui.QLabel(self.uiNIOVDESettingsGroupBox)
        self.uiVDELocalFileLabel.setObjectName(_fromUtf8("uiVDELocalFileLabel"))
        self.gridlayout12.addWidget(self.uiVDELocalFileLabel, 0, 0, 1, 1)
        self.uiVDELocalFileLineEdit = QtGui.QLineEdit(self.uiNIOVDESettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVDELocalFileLineEdit.sizePolicy().hasHeightForWidth())
        self.uiVDELocalFileLineEdit.setSizePolicy(sizePolicy)
        self.uiVDELocalFileLineEdit.setObjectName(_fromUtf8("uiVDELocalFileLineEdit"))
        self.gridlayout12.addWidget(self.uiVDELocalFileLineEdit, 1, 0, 1, 1)
        self.gridlayout10.addLayout(self.gridlayout12, 1, 0, 1, 1)
        self.gridlayout9.addWidget(self.uiNIOVDESettingsGroupBox, 0, 0, 1, 2)
        self.uiNIOVDEListGroupBox = QtGui.QGroupBox(self.tab_5)
        self.uiNIOVDEListGroupBox.setObjectName(_fromUtf8("uiNIOVDEListGroupBox"))
        self.vboxlayout5 = QtGui.QVBoxLayout(self.uiNIOVDEListGroupBox)
        self.vboxlayout5.setObjectName(_fromUtf8("vboxlayout5"))
        self.uiNIOVDEListWidget = QtGui.QListWidget(self.uiNIOVDEListGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNIOVDEListWidget.sizePolicy().hasHeightForWidth())
        self.uiNIOVDEListWidget.setSizePolicy(sizePolicy)
        self.uiNIOVDEListWidget.setObjectName(_fromUtf8("uiNIOVDEListWidget"))
        self.vboxlayout5.addWidget(self.uiNIOVDEListWidget)
        self.gridlayout9.addWidget(self.uiNIOVDEListGroupBox, 0, 2, 3, 1)
        self.uiAddNIOVDEPushButton = QtGui.QPushButton(self.tab_5)
        self.uiAddNIOVDEPushButton.setObjectName(_fromUtf8("uiAddNIOVDEPushButton"))
        self.gridlayout9.addWidget(self.uiAddNIOVDEPushButton, 1, 0, 1, 1)
        self.uiDeleteNIOVDEPushButton = QtGui.QPushButton(self.tab_5)
        self.uiDeleteNIOVDEPushButton.setEnabled(False)
        self.uiDeleteNIOVDEPushButton.setObjectName(_fromUtf8("uiDeleteNIOVDEPushButton"))
        self.gridlayout9.addWidget(self.uiDeleteNIOVDEPushButton, 1, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(161, 201, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridlayout9.addItem(spacerItem5, 2, 0, 2, 2)
        spacerItem6 = QtGui.QSpacerItem(196, 132, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout9.addItem(spacerItem6, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.gridlayout13 = QtGui.QGridLayout(self.tab_6)
        self.gridlayout13.setObjectName(_fromUtf8("gridlayout13"))
        self.uiNIONullSettingsGroupBox = QtGui.QGroupBox(self.tab_6)
        self.uiNIONullSettingsGroupBox.setObjectName(_fromUtf8("uiNIONullSettingsGroupBox"))
        self.gridlayout14 = QtGui.QGridLayout(self.uiNIONullSettingsGroupBox)
        self.gridlayout14.setObjectName(_fromUtf8("gridlayout14"))
        self.label_9 = QtGui.QLabel(self.uiNIONullSettingsGroupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridlayout14.addWidget(self.label_9, 0, 0, 1, 1)
        self.uiNIONullIdentiferLineEdit = QtGui.QLineEdit(self.uiNIONullSettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNIONullIdentiferLineEdit.sizePolicy().hasHeightForWidth())
        self.uiNIONullIdentiferLineEdit.setSizePolicy(sizePolicy)
        self.uiNIONullIdentiferLineEdit.setObjectName(_fromUtf8("uiNIONullIdentiferLineEdit"))
        self.gridlayout14.addWidget(self.uiNIONullIdentiferLineEdit, 1, 0, 1, 1)
        self.gridlayout13.addWidget(self.uiNIONullSettingsGroupBox, 0, 0, 1, 2)
        self.uiNIONullListGroupBox = QtGui.QGroupBox(self.tab_6)
        self.uiNIONullListGroupBox.setObjectName(_fromUtf8("uiNIONullListGroupBox"))
        self.vboxlayout6 = QtGui.QVBoxLayout(self.uiNIONullListGroupBox)
        self.vboxlayout6.setObjectName(_fromUtf8("vboxlayout6"))
        self.uiNIONullListWidget = QtGui.QListWidget(self.uiNIONullListGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNIONullListWidget.sizePolicy().hasHeightForWidth())
        self.uiNIONullListWidget.setSizePolicy(sizePolicy)
        self.uiNIONullListWidget.setObjectName(_fromUtf8("uiNIONullListWidget"))
        self.vboxlayout6.addWidget(self.uiNIONullListWidget)
        self.gridlayout13.addWidget(self.uiNIONullListGroupBox, 0, 2, 3, 1)
        self.uiAddNIONullPushButton = QtGui.QPushButton(self.tab_6)
        self.uiAddNIONullPushButton.setObjectName(_fromUtf8("uiAddNIONullPushButton"))
        self.gridlayout13.addWidget(self.uiAddNIONullPushButton, 1, 0, 1, 1)
        self.uiDeleteNIONullPushButton = QtGui.QPushButton(self.tab_6)
        self.uiDeleteNIONullPushButton.setEnabled(False)
        self.uiDeleteNIONullPushButton.setObjectName(_fromUtf8("uiDeleteNIONullPushButton"))
        self.gridlayout13.addWidget(self.uiDeleteNIONullPushButton, 1, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 261, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout13.addItem(spacerItem7, 2, 0, 2, 2)
        spacerItem8 = QtGui.QSpacerItem(20, 181, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout13.addItem(spacerItem8, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.gridLayout = QtGui.QGridLayout(self.tab_7)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.uiNameLabel = QtGui.QLabel(self.tab_7)
        self.uiNameLabel.setObjectName(_fromUtf8("uiNameLabel"))
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtGui.QLineEdit(self.tab_7)
        self.uiNameLineEdit.setObjectName(_fromUtf8("uiNameLineEdit"))
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 399, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.vboxlayout.addWidget(self.tabWidget)

        self.retranslateUi(cloudConfigPageWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(cloudConfigPageWidget)

    def retranslateUi(self, cloudConfigPageWidget):
        cloudConfigPageWidget.setWindowTitle(_translate("cloudConfigPageWidget", "Cloud configuration", None))
        self.uiGenericEthernetGroupBox.setTitle(_translate("cloudConfigPageWidget", "Generic Ethernet NIO (Administrator or root access required)", None))
        self.uiAddGenericEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Add", None))
        self.uiDeleteGenericEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Delete", None))
        self.uiLinuxEthernetGroupBox.setTitle(_translate("cloudConfigPageWidget", "Linux Ethernet NIO (Linux only, root access required)", None))
        self.uiAddLinuxEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Add", None))
        self.uiDeleteLinuxEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("cloudConfigPageWidget", "NIO Ethernet", None))
        self.uiNIOUDPSettingsGroupBox.setTitle(_translate("cloudConfigPageWidget", "Settings", None))
        self.uiLocalPortLabel.setText(_translate("cloudConfigPageWidget", "Local port:", None))
        self.uiRemoteHostLabel.setText(_translate("cloudConfigPageWidget", "Remote host:", None))
        self.uiRemoteHostLineEdit.setText(_translate("cloudConfigPageWidget", "127.0.0.1", None))
        self.uiRemotePortLabel.setText(_translate("cloudConfigPageWidget", "Remote port:", None))
        self.uiNIOUDPListGroupBox.setTitle(_translate("cloudConfigPageWidget", "NIOs", None))
        self.uiAddNIOUDPPushButton.setText(_translate("cloudConfigPageWidget", "&Add", None))
        self.uiDeleteNIOUDPPushButton.setText(_translate("cloudConfigPageWidget", "&Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("cloudConfigPageWidget", "NIO UDP", None))
        self.uiNIOTAPGroupBox.setTitle(_translate("cloudConfigPageWidget", "TAP interface (require root access)", None))
        self.uiAddNIOTAPPushButton.setText(_translate("cloudConfigPageWidget", "&Add", None))
        self.uiDeleteNIOTAPPushButton.setText(_translate("cloudConfigPageWidget", "&Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("cloudConfigPageWidget", "NIO TAP", None))
        self.uiNIOUNIXSettingsGroupBox.setTitle(_translate("cloudConfigPageWidget", "Settings", None))
        self.uiLocalFileLabel.setText(_translate("cloudConfigPageWidget", "Local file:", None))
        self.uiRemoteFileLabel.setText(_translate("cloudConfigPageWidget", "Remote file:", None))
        self.uiNIOUNIXListGroupBox.setTitle(_translate("cloudConfigPageWidget", "NIOs", None))
        self.uiAddNIOUNIXPushButton.setText(_translate("cloudConfigPageWidget", "&Add", None))
        self.uiDeleteNIOUNIXPushButton.setText(_translate("cloudConfigPageWidget", "&Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("cloudConfigPageWidget", "NIO UNIX", None))
        self.uiNIOVDESettingsGroupBox.setTitle(_translate("cloudConfigPageWidget", "Settings", None))
        self.uiVDEControlFileLabel.setText(_translate("cloudConfigPageWidget", "Control file:", None))
        self.uiVDELocalFileLabel.setText(_translate("cloudConfigPageWidget", "Local file:", None))
        self.uiNIOVDEListGroupBox.setTitle(_translate("cloudConfigPageWidget", "NIOs", None))
        self.uiAddNIOVDEPushButton.setText(_translate("cloudConfigPageWidget", "&Add", None))
        self.uiDeleteNIOVDEPushButton.setText(_translate("cloudConfigPageWidget", "&Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("cloudConfigPageWidget", "NIO VDE", None))
        self.uiNIONullSettingsGroupBox.setTitle(_translate("cloudConfigPageWidget", "Settings", None))
        self.label_9.setText(_translate("cloudConfigPageWidget", "Identifier:", None))
        self.uiNIONullListGroupBox.setTitle(_translate("cloudConfigPageWidget", "NIOs", None))
        self.uiAddNIONullPushButton.setText(_translate("cloudConfigPageWidget", "&Add", None))
        self.uiDeleteNIONullPushButton.setText(_translate("cloudConfigPageWidget", "&Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("cloudConfigPageWidget", "NIO NULL", None))
        self.uiNameLabel.setText(_translate("cloudConfigPageWidget", "Name:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("cloudConfigPageWidget", "Misc.", None))
