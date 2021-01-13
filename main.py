import pygame,sys,random


blockH = 10
blockW = 150

score = 0
speed = 2


#block object
class Block:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.w = blockW
        self.h = blockH
        self.color = color
        self.speed = speed

    def draw(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))

    def move(self):
        self.x += self.speed
        if self.x > width :
            self.speed *= -1
        if self.x + self.w < 1:
            self.speed *= -1


#tower object
class Tower:
    def __init__(self):
        global colorIndex
        self.tower = []
        self.initSize = 15
        for i in range(self.initSize):
            newBlock = Block(width/2 - blockW/2, height - (i + 1)*blockH, color[colorIndex], 0)
            colorIndex += 1
            self.tower.append(newBlock)

    def show(self):
        for i in range(self.initSize):
            self.tower[i].draw()

    def move(self):
        for i in range(self.initSize):
            self.tower[i].move()

    def addNewBlock(self):
        global colorIndex, speed

        if colorIndex >= len(color):
            colorIndex = 0
        
        y = self.peek().y
        if score > 50:
            speed += 0
        elif score%3 == 0:
            speed += 0.5
        
        newBlock = Block(width, y - blockH, color[colorIndex], speed)
        colorIndex += 1
        self.initSize += 1
        self.tower.append(newBlock)
        
    def peek(self):
        return self.tower[self.initSize - 1]

    def pushToTower(self):
        global blockW, score
        b = self.tower[self.initSize - 2]
        b2 = self.tower[self.initSize - 1]
        if b2.x <= b.x and not (b2.x + b2.w < b.x):
            self.tower[self.initSize - 1].w = self.tower[self.initSize - 1].x + self.tower[self.initSize - 1].w - b.x
            self.tower[self.initSize - 1].x = b.x
            if self.tower[self.initSize - 1].w > b.w:
                self.tower[self.initSize - 1].w = b.w
            self.tower[self.initSize - 1].speed = 0
            score += 1
        elif b.x <= b2.x <= b.x + b.w:
            self.tower[self.initSize - 1].w = b.x + b.w - b2.x
            self.tower[self.initSize - 1].speed = 0
            score += 1
        else:
            gameOver()
        for i in range(self.initSize):
            self.tower[i].y += blockH

        blockW = self.tower[self.initSize - 1].w

pygame.init()

width = 400
height = 500
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

bg_hor=pygame.image.load('hor.jpg')
bg_ver=pygame.image.load('vert.jpg')
background = (0, 0, 0)
Neon = (106, 255, 77)

# Color Codes
color = [(255,77,77),(255,106,77),(255,136,77),(255,166,77),(255,195,77),(255,225,77),
        (255,255,77),(225,255,77),(196,255,77),(166,255,77),(136,255,77),(106,255,77),(77,255,77),
        (77,255,106),(77,255,136),(77,255,166),(77,255,195),(77,255,225),(77,255,255),
        (77,225,255),(77,195,255),(77,166,255),(77,136,255),(77,106,255),(77,77,255),
        (106,77,255),(136,77,255),(166,77,255),(196,77,255),(225,77,255),(255,77,255),
        (255,77,225),(255,77,196),(255,77,166),(255,77,136),(255,77,106)]
#random.shuffle(color)
colorIndex = 0

# End game
def gameOver():
    loop = True 
    

    font = pygame.font.SysFont("Agency FB",50)
    text = font.render("Game Over! LOL", True, (255,25,25))
    
    textRect = text.get_rect()
    textRect.center = (width/2, height/2 - 80)
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    gameLoop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameLoop()
        display.blit(text, textRect)
        
        pygame.display.update()
        clock.tick()

# score
def showScore():
    font = pygame.font.SysFont("Agency FB", 30)
    text = font.render("Score: " + str(score), True, Neon)
    display.blit(text, (width/2 - 50,50))


#main game
def gameLoop():
    global blockW, blockH, score, colorIndex, speed
    loop = True

    blockH = 10
    blockW = 100
    colorIndex = 0
    speed = 3

    score = 0

    tower = Tower()
    tower.addNewBlock()
    

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    gameLoop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                tower.pushToTower()
                tower.addNewBlock()
                
        
        display.fill(background)
        display.blit(bg_hor,(0,0))
        display.blit(bg_ver,(0,0))
        #display.blit(bg_hor,(0,height-25))
        display.blit(bg_ver,(width-25,0))

        tower.move()
        tower.show()

        showScore()
        
        pygame.display.update()
        clock.tick(60)


#game starts now
gameLoop()