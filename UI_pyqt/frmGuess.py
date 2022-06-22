# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\lab11.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmGuess(object):
    def setupUi(self, frmGuess):
        frmGuess.setObjectName("frmGuess")
        frmGuess.resize(704, 323)
        self.guess_button = QtWidgets.QPushButton(frmGuess)
        self.guess_button.setGeometry(QtCore.QRect(90, 60, 121, 51))
        self.guess_button.setObjectName("guess_button")
        self.hint_button = QtWidgets.QPushButton(frmGuess)
        self.hint_button.setGeometry(QtCore.QRect(420, 60, 121, 51))
        self.hint_button.setObjectName("hint_button")
        self.guess_TextLabel = QtWidgets.QLabel(frmGuess)
        self.guess_TextLabel.setGeometry(QtCore.QRect(100, 170, 81, 31))
        self.guess_TextLabel.setObjectName("guess_TextLabel")
        self.timesGuessedLabel = QtWidgets.QLabel(frmGuess)
        self.timesGuessedLabel.setGeometry(QtCore.QRect(430, 160, 81, 31))
        self.timesGuessedLabel.setObjectName("timesGuessedLabel")

        self.retranslateUi(frmGuess)
        QtCore.QMetaObject.connectSlotsByName(frmGuess)

    def retranslateUi(self, frmGuess):
        _translate = QtCore.QCoreApplication.translate
        frmGuess.setWindowTitle(_translate("frmGuess", "Guess a number between 1 and 100"))
        self.guess_button.setText(_translate("frmGuess", "Guess..."))
        self.hint_button.setText(_translate("frmGuess", "Give me a hint..."))
        self.guess_TextLabel.setText(_translate("frmGuess", "Number of guesses: "))
        self.timesGuessedLabel.setText(_translate("frmGuess", "TextLabel"))


