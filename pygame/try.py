#只是當作測試
import pygame
import sys
import random
import time

from pygame.draw import rect
# 從pygame模組匯入常用的函式和常量
from pygame.locals import *

pygame.init()
# 初始化一個遊戲介面視窗
DISPLAY = pygame.display.set_mode((640, 480))
# 設定遊戲視窗的標題
pygame.display.set_caption('我試試看')
# 定義一個變數來控制遊戲速度
FPSCLOCK = pygame.time.Clock()
# 初始化遊戲介面內使用的字型
BASICFONT = pygame.font.SysFont("SIMYOU.TTF", 80)

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
PINK = pygame.Color(255, 150, 150)
GREY = pygame.Color(150, 150, 150)

def drawany():
    any = pygame.draw.rect(DISPLAY,PINK,Rect(320,100,20,20))
def drawtitle():
    title = BASICFONT.render("hozi", True, PINK)
    retitle = title.get_rect()
    retitle.midtop(320,240)
    DISPLAY.blit(title,retitle)

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAY.fill(GREY)
    drawany()
    #drawtitle()
    #重新整理Pygame的顯示層
    #沒有flip 顯示器不會顯示紅色
    pygame.display.flip()