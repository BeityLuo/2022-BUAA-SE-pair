# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import  os
from ctypes import *

dll = cdll.LoadLibrary(r"C:\Users\86182\Desktop\pair_dll.dll")

class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.mapping = {0: " -n", 1: " -w", 2: " -m", 3: " -c", 4: " -h", 5: " -t", 6: " -r"}
        self.l = [False for _ in range(7)]
        self.txt = ""
        self.result = ""
        self.cwd = os.getcwd()
        self.sel_file_name = ""
        self.save_file_name = ""
        self.sel_filetype = ""
        self.save_filetype = ""
        self.run_result = ""
        self.no = 0



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 652)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_5.setVisible(False)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit.setVisible(False)
        self.lineEdit.setDisabled(True)
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_6.setVisible(False)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_2.setVisible(False)
        self.lineEdit_2.setDisabled(True)
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 信号连接
        # btn
        self.pushButton.clicked.connect(self.btn_select_file)  # 选择
        self.pushButton_4.clicked.connect(self.btn_input_words)  # 导入
        self.pushButton_2.clicked.connect(self.btn_run_dll)  # 运行
        self.pushButton_3.clicked.connect(self.btn_save_file)  # 导出

        self.checkBox.stateChanged.connect(self.checkbox_choose0)
        self.checkBox_2.stateChanged.connect(self.checkbox_choose1)
        self.checkBox_3.stateChanged.connect(self.checkbox_choose2)
        self.checkBox_4.stateChanged.connect(self.checkbox_choose3)
        self.checkBox_5.stateChanged.connect(self.checkbox_choose4)
        self.checkBox_6.stateChanged.connect(self.checkbox_choose5)
        self.checkBox_7.stateChanged.connect(self.checkbox_choose6)

        # textEdit
        # 存在效率问题
        self.textEdit.textChanged.connect(self.txt_content_change)
    def btn_select_file(self):
        self.sel_file_name, self.sel_filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                              "选取文件",
                                                                              self.cwd,
                                                                              "Text Files (*.txt)")
        self.label.setText("选择的文件: " + self.file_name)


    def btn_input_words(self):
        if not os.path.isfile(self.sel_file_name):
            QtWidgets.QMessageBox.critical(self, "错误", "文件" + self.sel_file_name + "不存在!")
        else:
            f = open(self.sel_file_name, 'r')
            # 文件占用异常？
            try:
                print("进行读")
                all_the_text = f.read()
                print(all_the_text)
                self.txt = all_the_text
                self.textEdit.setText(all_the_text)
            except:
                QtWidgets.QMessageBox.critical(self, "错误", "文件内容过长!")
            finally:
                f.close()

    def btn_run_dll(self):
        #TODO some checks on conflicts between options & input

        ok = True
        if self.l[0]:
            if self.l[1] or self.l[2] or self.l[3] or self.l[4] or self.l[5] or self.l[6]:
                QtWidgets.QMessageBox.critical(self, "错误", "-n 不可与其他选项连用！")
                ok = False
        elif self.l[1]:
            if self.l[2] or self.l[3]:
                QtWidgets.QMessageBox.critical(self, "错误", "-w 不可与-m -c选项连用！")
                ok = False
            if self.l[4] and len(self.lineEdit.text()) != 1:
                QtWidgets.QMessageBox.critical(self, "错误", "-h 参数格式有误！")
                ok = False
            elif self.l[4] and not self.lineEdit.text().isalpha():
                QtWidgets.QMessageBox.critical(self, "错误", "-h 参数不是字母")
                ok = False
            if self.l[5] and len(self.lineEdit_2.text()) != 1:
                QtWidgets.QMessageBox.critical(self, "错误", "-t 参数格式有误！")
                ok = False
            elif self.l[5] and not self.lineEdit_2.text().isalpha():
                QtWidgets.QMessageBox.critical(self, "错误", "-t 参数不是字母")
                ok = False
        elif self.l[2]:
            if self.l[3]:
                QtWidgets.QMessageBox.critical(self, "错误", "-m 不可与其他选项连用！")
                ok = False
        elif self.l[3]:
            if self.l[4] and len(self.lineEdit.text()) != 1 :
                QtWidgets.QMessageBox.critical(self, "错误", "-h 参数格式有误！")
                ok = False
            elif self.l[4] and not self.lineEdit.text().isalpha():
                QtWidgets.QMessageBox.critical(self, "错误", "-h 参数不是字母")
                ok = False

            if self.l[5] and len(self.lineEdit_2.text()) != 1:
                QtWidgets.QMessageBox.critical(self, "错误", "-h 参数格式有误！")
                ok = False
            elif self.l[5] and not self.lineEdit_2.text().isalpha():
                QtWidgets.QMessageBox.critical(self, "错误", "-t 参数不是字母")
                ok = False
        elif self.l[4] or self.l[5] or self.l[6]:
            QtWidgets.QMessageBox.critical(self, "错误", "-h -t -r 不可缺少-n -m -w -c而单独使用！")
            ok = False
        else:
            QtWidgets.QMessageBox.critical(self, "错误", "请选择启动选项")

        if ok:
            if self.l[0]: #-n
                func = dll.gen_chains_all_python
                func.argtypes = [c_char_p, POINTER(c_char_p), POINTER(c_char_p)]
                func.restype = c_int
                STR = (c_char * len(self.txt))(*bytes(self.txt, 'utf-8'))
                cast(STR, c_char_p)
                szProgSize = create_string_buffer(20000)
                pszProgSize = c_char_p(addressof(szProgSize))
                errProgSize = create_string_buffer(20000)
                perrProgSize = c_char_p(addressof(errProgSize))
                print(func(STR, pszProgSize, perrProgSize))
                if bytes.decode(errProgSize.value) == '':
                    print(bytes.decode(szProgSize.value))
                    self.run_result = bytes.decode(szProgSize.value)
                    self.textBrowser.setText(bytes.decode(szProgSize.value))
                else:
                    print(bytes.decode(errProgSize.value))
                    self.run_result = bytes.decode(errProgSize.value)
                    self.textBrowser.setText(bytes.decode(errProgSize.value))
            elif self.l[1]: # -w
                func = dll.gen_chain_word_python
                func.argtypes = [c_char_p, POINTER(c_char_p), c_char, c_char, c_bool, POINTER(c_char_p)]
                func.restype = c_int
                STR = (c_char * len(self.txt))(*bytes(self.txt, 'utf-8'))
                szProgSize = create_string_buffer(20000)
                pszProgSize = c_char_p(addressof(szProgSize))
                errProgSize = create_string_buffer(20000)
                perrProgSize = c_char_p(addressof(errProgSize))
                cast(STR, c_char_p)
                ch1 = ""
                ch2 = ""
                head = 0
                tail = 0
                if self.l[4]:
                    ch1 = self.lineEdit.text()
                    if len(ch1) > 1:
                        ""
                    elif len(ch1) == 0:
                        ""
                    else:
                        head = ord(ch1[0])
                if self.l[5]:
                    ch2 = self.lineEdit_2.text()
                    if len(ch2) > 1:
                        ""
                    elif len(ch2) == 0:
                        ""
                    else:
                        tail = ord(ch2[0])

                print(func(STR, pszProgSize, c_char(head), c_char(tail), self.l[6], perrProgSize))
                if bytes.decode(errProgSize.value) == '':
                    print(bytes.decode(szProgSize.value))
                    self.run_result = bytes.decode(szProgSize.value)
                    self.textBrowser.setText(bytes.decode(szProgSize.value))
                else:
                    print(bytes.decode(errProgSize.value))
                    self.run_result = bytes.decode(errProgSize.value)
                    self.textBrowser.setText(bytes.decode(errProgSize.value))
            elif self.l[2]:
                func = dll.gen_chain_word_unique_python
                func.argtypes = [c_char_p, POINTER(c_char_p), POINTER(c_char_p)]
                func.restype = c_int
                STR = (c_char * len(self.txt))(*bytes(self.txt, 'utf-8'))
                szProgSize = create_string_buffer(20000)
                pszProgSize = c_char_p(addressof(szProgSize))
                errProgSize = create_string_buffer(20000)
                perrProgSize = c_char_p(addressof(errProgSize))
                cast(STR, c_char_p)
                print(func(STR, pszProgSize, perrProgSize))
                if bytes.decode(errProgSize.value) == '':
                    print(bytes.decode(szProgSize.value))
                    self.run_result = bytes.decode(szProgSize.value)
                    self.textBrowser.setText(bytes.decode(szProgSize.value))
                else:
                    print(bytes.decode(errProgSize.value))
                    self.run_result = bytes.decode(errProgSize.value)
                    self.textBrowser.setText(bytes.decode(errProgSize.value))
            elif self.l[3]:
                func = dll.gen_chain_char_python
                func.argtypes = [c_char_p, POINTER(c_char_p), c_char, c_char, c_bool, POINTER(c_char_p)]
                func.restype = c_int
                STR = (c_char * len(self.txt))(*bytes(self.txt, 'utf-8'))
                szProgSize = create_string_buffer(20000)
                pszProgSize = c_char_p(addressof(szProgSize))
                errProgSize = create_string_buffer(20000)
                perrProgSize = c_char_p(addressof(errProgSize))
                cast(STR, c_char_p)
                ch1 = ""
                ch2 = ""
                head = 0
                tail = 0
                if self.l[4]:
                    ch1 = self.lineEdit.text()
                    if len(ch1) > 1:
                        ""
                    elif len(ch1) == 0:
                        ""
                    else:
                        head = ord(ch1[0])
                if self.l[5]:
                    ch2 = self.lineEdit_2.text()
                    if len(ch2) > 1:
                        ""
                    elif len(ch2) == 0:
                        ""
                    else:
                        tail = ord(ch2[0])

                print(func(STR, pszProgSize, c_char(head), c_char(tail), self.l[6], perrProgSize))
                if bytes.decode(errProgSize.value) == '':
                    print(bytes.decode(szProgSize.value))
                    self.run_result = bytes.decode(szProgSize.value)
                    self.textBrowser.setText(bytes.decode(szProgSize.value))
                else:
                    print(bytes.decode(errProgSize.value))
                    self.run_result = bytes.decode(errProgSize.value)
                    self.textBrowser.setText(bytes.decode(errProgSize.value))
        return

    def btn_save_file(self):
        self.save_file_name, self.save_filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                              "选取文件",
                                                                              self.cwd,
                                                                              "Text Files (*.txt)")
        if os.path.isfile(self.save_file_name):
            QtWidgets.QMessageBox.critical(self, "错误", "文件名已存在!")
        else:
            fo = open(self.save_file_name, "w")
            fo.write(self.run_result)
            fo.close()
        return

    def txt_content_change(self):
        self.txt = self.textEdit.toPlainText()

    def checkbox_choose0(self):
        self.l[0] = self.checkBox.checkState() == QtCore.Qt.CheckState.Checked

    def checkbox_choose1(self):
        self.l[1] = self.checkBox_2.checkState() == QtCore.Qt.CheckState.Checked

    def checkbox_choose2(self):
        self.l[2] = self.checkBox_3.checkState() == QtCore.Qt.CheckState.Checked

    def checkbox_choose3(self):
        self.l[3] = self.checkBox_4.checkState() == QtCore.Qt.CheckState.Checked

    def checkbox_choose4(self):
        self.l[4] = self.checkBox_5.checkState() == QtCore.Qt.CheckState.Checked
        if self.l[4]:
            self.label_5.setVisible(True)
            self.lineEdit.setVisible(True)
            self.lineEdit.setDisabled(False)
        else:
            self.label_5.setVisible(False)
            self.lineEdit.setVisible(False)
            self.lineEdit.setDisabled(True)
            self.lineEdit.setText("")

    def checkbox_choose5(self):
        self.l[5] = self.checkBox_6.checkState() == QtCore.Qt.CheckState.Checked
        if self.l[5]:
            self.label_6.setVisible(True)
            self.lineEdit_2.setVisible(True)
            self.lineEdit_2.setDisabled(False)
        else:
            self.label_6.setVisible(False)
            self.lineEdit_2.setVisible(False)
            self.lineEdit_2.setDisabled(True)
            self.lineEdit_2.setText("")

    def checkbox_choose6(self):
        self.l[6] = self.checkBox_7.checkState() == QtCore.Qt.CheckState.Checked

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "选择的文件:"))
        self.pushButton.setText(_translate("Form", "选择文件"))
        self.pushButton_4.setText(_translate("Form", "导入(会自动覆盖已写入的单词)"))
        self.label_4.setText(_translate("Form", "或在下方输入单词:"))
        self.label_2.setText(_translate("Form", "启动选项:"))
        self.checkBox.setText(_translate("Form", "-n"))
        self.checkBox_2.setText(_translate("Form", "-w"))
        self.checkBox_3.setText(_translate("Form", "-m"))
        self.checkBox_4.setText(_translate("Form", "-c"))
        self.checkBox_5.setText(_translate("Form", "-h"))
        self.label_5.setText(_translate("Form", "输入-h参数"))
        self.checkBox_6.setText(_translate("Form", "-t"))
        self.label_6.setText(_translate("Form", "输入-t参数"))
        self.checkBox_7.setText(_translate("Form", "-r"))
        self.pushButton_2.setText(_translate("Form", "运行"))
        self.label_3.setText(_translate("Form", "运行结果:"))
        self.pushButton_3.setText(_translate("Form", "导出结果"))


if __name__ == "__main__":
 app = QtWidgets.QApplication(sys.argv)
 widget = QtWidgets.QWidget()
 ui = Ui_Form()
 ui.setupUi(widget)
 widget.show()
 sys.exit(app.exec_())