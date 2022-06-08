from PIL import Image
import os

# create a file(IMG_5461) that store every png of this gif
gifFileName="./woozi_img.GIF"
im = Image.open(gifFileName)
pngDir = gifFileName[:-4]
if not os.path.exists(pngDir):
    os.makedirs('./woozi_img')

try:
    while True:
        current = im.tell()
        im.save(pngDir+'/'+str(current+1)+'.png')
        im.seek(current+1)
except EOFError:
    pass

#改變圖片大小
file_list = os.listdir("./woozi_img")
#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
#print(file_list)
n = len(file_list)
for i in range(n):
    s = str(file_list[i])
    if s[-4:] == ".png":
        src = os.path.join(os.path.abspath('./woozi_img/'),s)
        img = Image.open(src)
        new_img = img.resize((300,300),Image.BILINEAR)#原360x360
        new_img.save(src)

#初始化桌面掛件

import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui

class DesktopPet(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(DesktopPet, self).__init__(parent)
        # 初始化
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.repaint()
        self.pet_images = self.loadImage('./woozi_img/1.png')
        #放圖
        self.image = QLabel(self)
        self.setImage(self.pet_images)
        #退出
        self.iconpath1 = './woozi_img/icon.jpeg'
        self.iconpath2 = './woozi_img/icon2.jpeg'
        quit_action = QAction('關了拉靠北喔', self, triggered=self.quit)
        quit_action.setIcon(QIcon(self.iconpath1))
        quit_action2 = QAction('這也是一樣的行為拉搞屁喔', self, triggered=self.quit)
        quit_action2.setIcon(QIcon(self.iconpath1))
        self.tray_icon_menu = QMenu(self)
        self.tray_icon_menu.addAction(quit_action)
        self.tray_icon_menu.addAction(quit_action2)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(self.iconpath2))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()

        self.resize(300, 300)
        self.randomPosition()
        self.show()

        #是否跟随鼠标
        self.is_follow_mouse = False
        # 宠物拖拽时避免鼠标直接跳到左上角
        self.mouse_drag_pos = self.pos()
        self.pointer = 1
        # 每隔一段时间做个动作
        self.timer = QTimer()
        self.timer.timeout.connect(self.runFrame)
        self.timer.start(50)
        

    def randomPosition(self):
        screen_geo = QDesktopWidget().screenGeometry()
        pet_geo = self.geometry()
        width = (screen_geo.width() - pet_geo.width()) * random.random()
        height = (screen_geo.height() - pet_geo.height()) * random.random()
        self.move(width, height)

    def loadImage(self, imagepath):
        image = QImage()
        image.load(imagepath)
        return image
    
    def setImage(self, image):
        self.image.setPixmap(QPixmap.fromImage(image))

    def quit(self):
        self.close()
        sys.exit()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
            self.mouse_drag_pos = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.mouse_drag_pos)
            event.accept()
    

    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    def runFrame(self):
        path = './woozi_img/{img}.png'.format(img=self.pointer)
        img = self.loadImage(path)
        self.setImage(img)
        self.pointer+=1
        if self.pointer > 66:
            self.pointer=1
	

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = DesktopPet()
    sys.exit(app.exec_())

