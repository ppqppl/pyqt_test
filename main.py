# python
# -*- coding: UTF-8 -*-
'''
@Author  ：ppqppl
@Date    ：2022/9/9 12:12
'''

import sys
from PyQt5.Qt import *
import requests
import pic
from PIL import Image

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.ui = pic.Ui_MainForm()
        self.ui.setupUi(self)
        # self.addui(self)
        self.bind_trigger(self)
    # def addui(self):
        # self.
    def bind_trigger(self,event):
        self.ui.LoadPicButton.clicked.connect(self.click_LoadPicButton)  # 按钮绑定鼠标左键点击事件  图片加载事件
        self.ui.SavePicButton.clicked.connect(self.click_SavePicButton)  # 图片保存事件
    def click_LoadPicButton(self):
        global LoadPicName
        LoadPicName, filetype = QFileDialog.getOpenFileName(self, "选择图片", "C://Users//ppqpp//Pictures","Pic Files (*.jpg;*.jeg;*.png;*.gif);;All Files (*);")  # 设置文件扩展名过滤,注意用双分号间隔
        print(LoadPicName)
        img = Image.open(LoadPicName)
        # img = ImageQt.toqpixmap(img)
        # qimage = ImageQt.ImageQt(img)
        # self.label_2.setPixmap(img)

    def click_SavePicButton(self):
        global LoadPicName
        SavePicName, filetype = QFileDialog.getSaveFileName(self,"保存图片","C://Users//ppqpp//Pictures","Pic Files (*.jpg;*.jeg;*.png;*.gif);;All Files (*);")  # 设置文件扩展名过

def func():
    print("HelloWorld")


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    myForm = MainWindow()
    myForm.show()
    sys.exit(myapp.exec_())
