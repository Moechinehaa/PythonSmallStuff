import pygame
import sys
import random
import time
# 從pygame模組匯入常用的函式和常量
from pygame.locals import * 

# 初始化Pygame庫
pygame.init()
# 初始化一個遊戲介面視窗
DISPLAY = pygame.display.set_mode((640, 480))
# 設定遊戲視窗的標題
pygame.display.set_caption('末葉清貪吃蛇小遊戲拉')
# 定義一個變數來控制遊戲速度
FPSCLOCK = pygame.time.Clock()
# 初始化遊戲介面內使用的字型
BASICFONT = pygame.font.SysFont("SIMYOU.TTF", 80)

# 定義顏色變數
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)

# 貪吃蛇的的初始位置
snake_Head = [100,100]
# 初始化貪吃蛇的長度 (注：這裡以20*20為一個標準小格子)
snake_Body = [[80,100],[60,100],[40,100]]
# 指定蛇初始前進的方向，向右
direction = "right"

# 給定第一枚食物的位置
food_Position = [300,300]
# 食物標記：0代表食物已被吃掉；1代表未被吃掉。
food_flag = 1

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

ptime = 7
body=5

# 繪製貪吃蛇
def drawSnake(snake_Body):
    for i in snake_Body:
        pygame.draw.rect(DISPLAY, WHITE, Rect(i[0], i[1], 20, 20))
# 繪製食物的位置
def drawFood(food_Position):
    pygame.draw.rect(DISPLAY, RED, Rect(food_Position[0], food_Position[1], 20, 20))

# 列印出當前得分
def drawScore(score):
    # 設定分數的顯示顏色
    score_Surf = BASICFONT.render('%s' %(score), True, GREY)
    # 設定分數的位置
    score_Rect = score_Surf.get_rect()
    score_Rect.midtop = (320, 240)
    # 繫結以上設定到控制程式碼
    DISPLAY.blit(score_Surf, score_Rect)

    '''
    #改字體、大小
    字體變數 = pygame.font.SysFont(字體名稱, 字體尺寸)
    #繪製
    文字變數 = 字體變數.render(文字, 平滑值, 文字顏色, 背景顏色)
    '''
# 遊戲結束並退出
def GameOver():
    # 設定GameOver的顯示顏色
    GameOver_Surf = BASICFONT.render('Game Over!', True, GREY)
    # 設定GameOver的位置
    GameOver_Rect = GameOver_Surf.get_rect()
    GameOver_Rect.midtop = (320, 10)
    # 繫結以上設定到控制程式碼
    DISPLAY.blit(GameOver_Surf, GameOver_Rect)

    pygame.display.flip()
    # 等待3秒
    time.sleep(3)
    # 退出遊戲
    pygame.quit()
    # 退出程式
    sys.exit()

#主程式
while 1:
# 檢測按鍵等Pygame事件
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件後，退出程式
            pygame.quit()
            sys.exit()
            
        # 判斷鍵盤事件，用 方向鍵 或 wsad 來表示上下左右
        elif event.type == KEYDOWN:
            if (event.key == K_UP or event.key == K_w) and direction != DOWN:
                direction = UP
            if (event.key == K_DOWN or event.key == K_s) and direction != UP:
                direction = DOWN
            if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                direction = LEFT
            if (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                direction = RIGHT
        
    # 根據鍵盤的輸入，改變蛇的頭部，進行轉彎操作
    if direction == LEFT:
        snake_Head[0] -= 20
    if direction == RIGHT:
        snake_Head[0] += 20
    if direction == UP:
        snake_Head[1] -= 20
    if direction == DOWN:
        snake_Head[1] += 20

    # 將蛇的頭部當前的位置加入到蛇身的列表中
    snake_Body.insert(0, list(snake_Head))

    # 判斷是否吃掉食物
    if snake_Head[0]==food_Position[0] and snake_Head[1]==food_Position[1]:
        food_flag = 0
    else:
        snake_Body.pop()
    
    # 生成新的食物
    if food_flag == 0:
        # 隨機生成x, y
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        food_Position = [int(x*20),int(y*20)]
        food_flag = 1
    
    DISPLAY.fill(BLACK)
    # 畫出貪吃蛇
    drawSnake(snake_Body)
    # 畫出食物的位置
    drawFood(food_Position)
    # 列印出玩家的分數
    drawScore(len(snake_Body) - 3)
    # 重新整理Pygame的顯示層，貪吃蛇與食物的每一次移動，都會進行重新整理顯示層的操作來顯示。
    pygame.display.flip()
    # 控制遊戲速度
    #15超快ㄟ哈哈好好玩
    #如果隨著關卡增加速度也很有趣
    if len(snake_Body)>3+body:
        ptime+=2
        body+=5
    FPSCLOCK.tick(ptime)

    '''遊戲結束的判斷'''
    # 貪吃蛇觸碰到邊界
    if snake_Head[0]<0 or snake_Head[0]>620:
        GameOver()
    if snake_Head[1]<0 or snake_Head[1]>460:
        GameOver()
    # 貪吃蛇觸碰到自己
    for i in snake_Body[1:]:
        if snake_Head[0]==i[0] and snake_Head[1]==i[1]:
            GameOver()
        