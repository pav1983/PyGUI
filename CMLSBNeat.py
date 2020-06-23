# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Phillip\OneDrive\GUI Projects\CMLSB\CMLSB.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 230)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 346, 209))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nova Flat")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.FU = QtWidgets.QPushButton(self.layoutWidget)
        self.FU.setMouseTracking(False)
        self.FU.setObjectName("FU")
        self.verticalLayout.addWidget(self.FU)
        self.Lockmeup = QtWidgets.QPushButton(self.layoutWidget)
        self.Lockmeup.setObjectName("Lockmeup")
        self.verticalLayout.addWidget(self.Lockmeup)
        self.Tryingtohelp = QtWidgets.QPushButton(self.layoutWidget)
        self.Tryingtohelp.setObjectName("Tryingtohelp")
        self.verticalLayout.addWidget(self.Tryingtohelp)
        self.Mathafucka = QtWidgets.QPushButton(self.layoutWidget)
        self.Mathafucka.setObjectName("Mathafucka")
        self.verticalLayout.addWidget(self.Mathafucka)
        self.Mathafuckaaaa = QtWidgets.QPushButton(self.layoutWidget)
        self.Mathafuckaaaa.setObjectName("Mathafuckaaaa")
        self.verticalLayout.addWidget(self.Mathafuckaaaa)
        self.BetterRepent = QtWidgets.QPushButton(self.layoutWidget)
        self.BetterRepent.setObjectName("BetterRepent")
        self.verticalLayout.addWidget(self.BetterRepent)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FUSir = QtWidgets.QPushButton(self.layoutWidget)
        self.FUSir.setObjectName("FUSir")
        self.verticalLayout_2.addWidget(self.FUSir)
        self.GAFMUPOS = QtWidgets.QPushButton(self.layoutWidget)
        self.GAFMUPOS.setObjectName("GAFMUPOS")
        self.verticalLayout_2.addWidget(self.GAFMUPOS)
        self.GTFOuttaHere = QtWidgets.QPushButton(self.layoutWidget)
        self.GTFOuttaHere.setObjectName("GTFOuttaHere")
        self.verticalLayout_2.addWidget(self.GTFOuttaHere)
        self.STFUBitch = QtWidgets.QPushButton(self.layoutWidget)
        self.STFUBitch.setObjectName("STFUBitch")
        self.verticalLayout_2.addWidget(self.STFUBitch)
        self.USOB = QtWidgets.QPushButton(self.layoutWidget)
        self.USOB.setDefault(False)
        self.USOB.setFlat(False)
        self.USOB.setObjectName("USOB")
        self.verticalLayout_2.addWidget(self.USOB)
        self.NBMTeeth = QtWidgets.QPushButton(self.layoutWidget)
        self.NBMTeeth.setObjectName("NBMTeeth")
        self.verticalLayout_2.addWidget(self.NBMTeeth)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Crazy Meijer Lady Soundboard"))
        self.FU.setText(_translate("Dialog", "Fuck You!"))
        self.Lockmeup.setText(_translate("Dialog", "You can lock me up...!"))
        self.Tryingtohelp.setText(_translate("Dialog", "I\'m trying to help you m..."))
        self.Mathafucka.setText(_translate("Dialog", "MuthaFucka"))
        self.Mathafuckaaaa.setText(_translate("Dialog", "Muthafuckaaaaaa"))
        self.BetterRepent.setText(_translate("Dialog", "Better Repent...!"))
        self.FUSir.setText(_translate("Dialog", "Fuck you, sir!"))
        self.GAFMUPOS.setText(_translate("Dialog", "Get the F away from me POS!"))
        self.GTFOuttaHere.setText(_translate("Dialog", "GTF outta here I told you!"))
        self.STFUBitch.setText(_translate("Dialog", "STFU, Bitch!"))
        self.USOB.setText(_translate("Dialog", "You sonofabitch!"))
        self.NBMTeeth.setText(_translate("Dialog", "Never brush my teeth!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


