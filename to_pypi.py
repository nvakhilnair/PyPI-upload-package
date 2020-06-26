
from PyQt4 import QtCore, QtGui
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


def main():
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

    class Ui_Pypip(QWidget):
        def setupUi(self, Pypip):
            Pypip.setObjectName(_fromUtf8("Pypip"))
            Pypip.resize(400, 300)

            Pypip.setAutoFillBackground(False)
            Pypip.setStyleSheet(
            "QWidget#Pypip {background-image: url('data/logo.png');background-repeat: no-repeat; background-position: bottom left;}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("data\icon.ico")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
            Pypip.setWindowIcon(icon)
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("MS Serif"))
            font.setBold(True)
            font.setWeight(75)
            Pypip.setFont(font)
            self.username = QtGui.QLineEdit(Pypip)
            self.username.setGeometry(QtCore.QRect(110, 110, 161, 20))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Times New Roman"))
            font.setBold(False)
            font.setWeight(50)
            self.username.setFont(font)
            self.username.setObjectName(_fromUtf8("username"))
            self.password = QtGui.QLineEdit(Pypip)
            self.password.setGeometry(QtCore.QRect(110, 150, 161, 20))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Times New Roman"))
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.password.setFont(font)
            self.password.setObjectName(_fromUtf8("password"))
            self.password.setEchoMode(QtGui.QLineEdit.Password)
            self.label = QtGui.QLabel(Pypip)
            self.label.setGeometry(QtCore.QRect(30, 110, 81, 20))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Times New Roman"))
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.label.setFont(font)
            self.label.setObjectName(_fromUtf8("label"))
            self.label_2 = QtGui.QLabel(Pypip)
            self.label_2.setGeometry(QtCore.QRect(30, 150, 71, 16))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Times New Roman"))
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.label_2.setFont(font)
            self.label_2.setObjectName(_fromUtf8("label_2"))
            self.test = QtGui.QRadioButton(Pypip)
            self.test.setGeometry(QtCore.QRect(120, 40, 82, 17))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Times New Roman"))
            font.setBold(False)
            font.setWeight(50)
            self.test.setFont(font)
            self.test.setChecked(True)
            self.test.setObjectName(_fromUtf8("test"))
            self.pypip = QtGui.QRadioButton(Pypip)
            self.pypip.setGeometry(QtCore.QRect(220, 40, 82, 17))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Times New Roman"))
            font.setBold(False)
            font.setWeight(50)
            self.pypip.setFont(font)
            self.pypip.setObjectName(_fromUtf8("pypip"))
            self.Select_directory = QtGui.QPushButton(Pypip)
            self.Select_directory.setGeometry(QtCore.QRect(110, 70, 101, 23))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Times New Roman"))
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.Select_directory.setFont(font)
            self.Select_directory.setObjectName(_fromUtf8("Select_directory"))
            self.Select_directory.clicked.connect(self.open_file)
            self.Upload = QtGui.QPushButton(Pypip)
            self.Upload.setGeometry(QtCore.QRect(140, 180, 111, 23))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Times New Roman"))
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.Upload.setFont(font)
            self.Upload.setObjectName(_fromUtf8("Upload"))
            self.Upload.clicked.connect(self.upload_data)
            self.exit = QtGui.QPushButton(Pypip)
            self.exit.setGeometry(QtCore.QRect(310, 250, 75, 23))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Times New Roman"))
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.exit.setFont(font)
            self.exit.setObjectName(_fromUtf8("exit"))
            self.exit.clicked.connect(self.exit_app)

            self.label_3 = QtGui.QLabel(Pypip)
            self.label_3.setGeometry(QtCore.QRect(10, 70, 101, 20))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Times New Roman"))
            font.setPointSize(11)
            font.setBold(False)
            font.setWeight(50)
            self.label_3.setFont(font)
            self.label_3.setObjectName(_fromUtf8("label_3"))
            self.label_4 = QtGui.QLabel(Pypip)
            self.label_4.setGeometry(QtCore.QRect(30, 40, 71, 16))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Times New Roman"))
            font.setPointSize(11)
            font.setBold(False)
            font.setWeight(50)
            self.label_4.setFont(font)
            self.label_4.setObjectName(_fromUtf8("label_4"))

            self.retranslateUi(Pypip)
            QtCore.QMetaObject.connectSlotsByName(Pypip)

        def exit_app(self):
            choice = QtGui.QMessageBox.question(self, 'Exit', "Do You want to exit",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                sys.exit()
            else:
                pass

        def open_file(self):
            global name
            name = QFileDialog.getOpenFileName(self, 'Open file',
                                               'c:\\', "setup.py (setup.py)")
            name = name[0:(len(name)-8)]

        def upload_data(self):
            username = self.username.text()
            password = self.password.text()
            if self.test.isChecked() == True:
                command = 'cd /d ' + name + ' &' + ' python setup.py sdist bdist_wheel & ' + \
                    'twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u ' + \
                    username + ' -p ' + password + ' >log.txt'
                os.system(command)

            else:
                command = 'cd /d ' + name + ' &' + ' python setup.py sdist bdist_wheel & ' + \
                    'twine upload --repository-url https://upload.pypi.org/legacy/ dist/* -u ' + \
                    username + ' -p ' + password + ' >log.txt'
                os.system(command)
            log_loc = name+'log.txt'
            with open(log_loc) as f:
                if 'View at:' in f.read():
                    sucess = QtGui.QMessageBox.information(
                        self, 'Sucess', "Sucessfull")
                else:
                    file_name = name + 'log.txt'
                    with open(file_name, "r") as myfile:
                        data = myfile.readlines()
                    data = str(data)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Authentication error or Version error Exist")
                    msg.setInformativeText(
                        "Please click show details for more details")
                    msg.setWindowTitle("Error")
                    msg.setDetailedText(data)
                    msg.setStandardButtons(QMessageBox.Ok)
                    retval = msg.exec_()
                    myfile.close()
            f.close()
            os.remove(log_loc)

        def retranslateUi(self, Pypip):
            Pypip.setWindowTitle(_translate("Pypip", "PyPI upload", None))
            self.label.setText(_translate("Pypip", "Username", None))
            self.label_2.setText(_translate("Pypip", "Password", None))
            self.test.setText(_translate("Pypip", "PyPI test", None))
            self.pypip.setText(_translate("Pypip", "PyPI", None))
            self.Select_directory.setText(
                _translate("Pypip", "Select Dirtectory", None))
            self.Upload.setText(_translate("Pypip", "Submit and upload", None))
            self.exit.setText(_translate("Pypip", "Exit", None))
            self.label_3.setText(_translate("Pypip", "Select Setup.py", None))
            self.label_4.setText(_translate("Pypip", "Upload To:", None))

    if __name__ == "__main__":
        import sys
        app = QtGui.QApplication(sys.argv)
        Pypip = QtGui.QDialog()
        ui = Ui_Pypip()
        ui.setupUi(Pypip)
        Pypip.show()
        sys.exit(app.exec_())


main()
