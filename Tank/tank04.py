import pygame
"""
mouse event
click botton close game
方向control  bullet shot

"""

_display=pygame.display
class MainGame():
    #游戏主窗口
    window=None
    SCREEN_WIDTH=800
    SCREEN_HEIGHT=500
    COLOR_BLACK=pygame.Color(0,0,0)
    COLOR_RED = pygame.Color(255, 0, 0)

    def getTextSurface(self,text):
        #初始化字体模块   选合适的字体
        pygame.font.init()
        # fontList=pygame.font.get_fonts()
        # print(fontList)
        font=pygame.font.SysFont("kaiti",18)
        textSruface=font.render(text,True,MainGame.COLOR_RED)
        return textSruface
        #使用相应的字体完成相关内容的绘制

    def __init__(self):
        pass
    def startGame(self):
        pygame.display.init()
        #self.getTextSurface('aaa')
        MainGame.window=_display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        #设置游戏标题
        _display.set_caption("坦克大战v1.03")
        while True:

            MainGame.window.fill(MainGame.COLOR_BLACK)
            self.getEvent()
            MainGame.window.blit(self.getTextSurface("剩余坦克数量%d"%5),(5,5))

            _display.update()



        pass

    def getEvent(self):
        """
        1.事件处理：获取所有事件
        2.对事件进行判断处理：（1）点击关闭按钮（2）按下键盘上的某个键
        :return:

        """
        eventList=pygame.event.get()
        for event in eventList:
            if event.type==pygame.QUIT:
                self.endGame()
            #判断按键类型是否为键盘按下，如果是，继续判断按键是哪一个，来进行对应处理
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    print("坦克向左掉头")
                elif event.key==pygame.K_d:
                    print("坦克向右掉头")
                elif event.key==pygame.K_w:
                    print("向上")
                elif event.key==pygame.K_s:
                    print("向下")
                elif event.key==pygame.K_SPACE:
                    print("发射子弹")
        pass
    def endGame(self):
        print("游戏结束")
        exit()
class Tank:
    def __init__(self):
        pass
    def move(self):
        pass
    def shot(self):
        pass
    def displayTank(self):
        pass

class MyTank(Tank):
    def __init__(self):
        pass

class classEnemyTank(Tank):
    def __init__(self):
        pass

class Bullet():
    def __init__(self):
        pass
    def move(self):
        pass
    def displayBullet(self):
        pass

class Explode():
    def __init__(self):
        pass
    def displayExplode(self):
        pass

class Wall():
    def __init__(self):
        pass
    def displayWall(self):
        pass

class Music():
    def __init__(self):
        pass
    def play(self):
        pass


MainGame().startGame()
