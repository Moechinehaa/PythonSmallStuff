import pygame
import math

import matplotlib.pyplot as plt
import numpy as np
import time

clock = pygame.time.Clock()

pygame.init()
display = pygame.display.set_mode((700,700))
display.fill((255,255,255))

pos_x = 350
pos_y = 350
sur_width = 350
sur_height = 175
width = sur_width/2
height = sur_height/2

sur = pygame.Surface((sur_width,sur_height))
sur.set_alpha(225)

#draw surface

display.blit(sur,(pos_x,pos_y))
pygame.draw.arc(display,(255,255,255),(pos_x,pos_y,sur_width,sur_width),0,math.pi+0.04,10)
for n in range(11):
    num = n*10
    angle = 0
    if(num!=0):
        angle = (num*math.pi)/100
    x = math.cos(angle)*(width-50) + (pos_x+width) -10
    y = -math.sin(angle)*(width-50) + (pos_y+width) -30
    font1 = pygame.font.Font(None,40)
    font_img=font1.render(str(100-num),True,(255,255,255))
    display.blit(font_img,(x,y))
    #speed
    speed = 100
    blit_speed = 100 - speed
    speed_angle = 0
    if(blit_speed!=0):
        speed_angle = (blit_speed*math.pi)/100
    sx = math.cos(speed_angle)*(width-70) + (pos_x+width)
    sy = -math.sin(speed_angle)*(width-70) + (pos_y+width) -30
    pygame.draw.line(display,(0,255,255),(pos_x+width,pos_y+width),(sx,sy),4)



def drawpoint(clock2):
    num = pygame.time.get_ticks()/60000
    acceleration=np.random.random()  #生成随机数画图
    throttle=10
    velocity=20
    #g1 替換成加速度數值
	#图表
    ax.append(num)      #追加x坐标值
    ay.append(acceleration)
    ay2.append(throttle)
    ay3.append(velocity)

def drawplot():
    fig = plt.figure(figsize = (8,8))
    fig.add_subplot(1,1,1)
    plt.suptitle("a-t graph",fontsize=30)
    agraphic=plt.subplot(2,1,1)
    #agraphic.set_title('')      #添加子标题
    agraphic.set_xlabel('time',fontsize=20)   #添加轴标签
    #agraphic.set_ylabel('', fontsize=20)
    plt.plot(ax,ay,'g-')                #等于agraghic.plot(ax,ay,'g-')
    plt.plot(ax,ay2,'m-')
    plt.plot(ax,ay3,'c-')
	
    plt.legend(['acceleration','throttle','velocity'])
    plt.show()



ax=[]   #保存图1数据
ay=[]
ay2=[]
ay3=[]
ay4=[]
num=0

#plt.ioff()
#plt.show()    

'''
delay_time = 1000 #1second
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event,delay_time)
'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawplot()
            pygame.quit()
            exit()
    
    drawpoint(clock)
    pygame.display.update()
