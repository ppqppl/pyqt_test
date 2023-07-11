# python
# -*- coding: UTF-8 -*-
'''
@Author  ：ppqppl
@Date    ：2022/9/11 13:50 
'''

from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, QtCore
import PIL
import os
import sys
import math
import requests

import Img
import ImgQuit


class MainWindow(Img.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Img.Ui_MainWindow()
        self.ui.setupUi(self)
        self.bind_trigger(self)
        self.setting_window(self)

    def setting_window(self,event):
        self.setWindowTitle("图片编辑器")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        _translate = QtCore.QCoreApplication.translate  # 给控件命名
        self.ui.toolBox.setItemText(self.ui.toolBox.indexOf(self.ui.page1), _translate("MainWindow", "基本处理"))
        self.ui.toolBox.setItemText(self.ui.toolBox.indexOf(self.ui.page2), _translate("MainWindow", "页面 2"))

    def bind_trigger(self,event):
        self.ui.actionLoad.triggered.connect(self.click_LoadPicButton)  # 按钮绑定鼠标左键点击事件  图片加载事件
        self.ui.actionSave.triggered.connect(self.click_SavePicButton)  # 图片保存事件
        self.ui.actionQuit.triggered.connect(self.click_QuitButton)
        self.ui.ClearButton.clicked.connect(self.click_ClearButton)
        self.ui.RenewButton.clicked.connect(self.click_RenewButton)
        self.ui.BrightnessSlider.valueChanged.connect(self.BrightnessSlider_move)
        self.ui.PicSizeSlider.valueChanged.connect(self.PicSizeSlider_move)

    def click_LoadPicButton(self):
        global LoadPicName
        LoadPicName, filetype = QFileDialog.getOpenFileName(self, "选择图片", "C://Users//ppqpp//Pictures",
                                                            "Pic Files (*.jpg;*.jepg;*.png;*.gif);;All Files (*);")  # 设置文件扩展名过滤,注意用双分号间隔
        print(LoadPicName)
        # self.click_ClearButton()
        global img_show
        img_show = PIL.Image.open(LoadPicName)
        self.ui.PicLabel.clear()
        # self.pic = QtGui.QPixmap(LoadPicName) # 直接读取图片并显示
        self.pic = PIL.ImageQt.topixmap(img_show) # 显示 PIL 图片
        self.pic = self.pic.scaled(self.ui.PicLabel.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.ui.PicLabel.setPixmap(self.pic)
        # self.ui.PicLabel.setScaledContents(True)    # 图片自适应 Qlabel 尺寸进行显示，不会降低清晰度

    def click_SavePicButton(self):
        print("Save")
        global LoadPicName
        SavePicName, filetype = QFileDialog.getSaveFileName(self,"保存图片","C://Users//ppqpp//Pictures",
                                                            "Pic Files (*./);;All Files (*);")
        if SavePicName != "":
            img = self.ui.PicLabel.pixmap().toImage()   # 使用控件截屏方法
            img.save(SavePicName)

    def click_QuitButton(self):
        print("确定退出？")
        quitdialog = QuitDialog()
        quitdialog.show()
        quitdialog.exec_()

    def click_ClearButton(self):
        print("清空界面")
        global LoadPicName
        LoadPicName = ""
        self.ui.PicLabel.clear()
        self.ui.PicLabel.setText("空白图片")
        self.ui.BrightnessSlider.setValue(0)

    def click_RenewButton(self):
        print("更新图片")
        self.ui.BrightnessSlider.setValue(0)
        self.ui.PicSizeSlider.setValue(50)

    def BrightnessSlider_move(self):
        global bright_percent
        bright_percent = float(self.ui.BrightnessSlider.value()/100)
        print(bright_percent)

    def PicSizeSlider_move(self):
        print(self.ui.PicSizeSlider.value())

    def wheelEvent(self, event):
        angel = event.angelData()/8 # 滚轮滑动角度的 1/8
        angely = angel.y()  # 滚轮 y 轴滚动角度

    def closeEvent(self, event):
        print("确定退出？")
        global ifQuitAll
        quitdialog = QuitDialog()
        quitdialog.show()
        quitdialog.exec_()
        if ifQuitAll == True:
            event.accept()
        else:
            event.ignore()

    def getBrightness(self):
        global LoadPicName
        img = PIL.Image.open(LoadPicName)
        stat= PIL.ImageStat.Stat(img)

    # def

class QuitDialog(ImgQuit.Ui_QuitDialog,QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(QuitDialog, self).__init__(parent)
        self.ui = ImgQuit.Ui_QuitDialog()
        self.ui.setupUi(self)
        self.bind_trigger(self)
        self.setting_window(self)

    def bind_trigger(self,event):
        self.ui.QuitButton.clicked.connect(self.click_QuitButton)
        self.ui.CancelButton.clicked.connect(self.click_CancelButton)

    def setting_window(self,event):
        self.setWindowTitle("退出")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.MSWindowsFixedSizeDialogHint | QtCore.Qt.WindowStaysOnTopHint)
        # 取消最小化和最大化及关闭按钮（利用固定大小方法） 最后一个参数用于设置窗口顶置

    def click_QuitButton(self,event):
        print("退出")
        global myForm,ifQuitAll
        ifQuitAll = True
        self.close()
        myForm.close()

    def click_CancelButton(self):
        print("取消退出")
        global ifQuitAll
        ifQuitAll = False
        self.close()

def func():
    print("HelloWorld")


if __name__ == "__main__":
    global myForm
    myapp = QtWidgets.QApplication(sys.argv)
    myForm = MainWindow()
    myForm.show()
    sys.exit(myapp.exec_())

### 灰度化、二值化、调节亮度