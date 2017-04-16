import pygame

# Создаем окно (присваеваем переменной window)
window = pygame.display.set_mode((800, 600))

# Название окна
pygame.display.set_caption('ver Alpha 0.1')

# Область действия
screen = pygame.Surface((800, 600))

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename) #загружаем картинку
        #self.bitmap.set_colorkey((255,255,255)) # какой цвет будет прозрачным
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

hero = Sprite(0, 0, "hero.png")
hero.go_right = True

zet = Sprite(270, 100, "m.png")

""" a = задержка перед первым дублированием
    b = задержка между остальными дублированиями
    считается в мс
"""

pygame.key.set_repeat(1, 1)


# Закрывашка
done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            #перемещение героя
            if e.key == pygame.K_LEFT:
                if hero.x > 0:
                    hero.x -= 1
            if e.key == pygame.K_RIGHT:
                if hero.x < (800-64):
                    hero.x += 1
            if e.key == pygame.K_UP:
                if hero.y > 0:
                    hero.y -= 1
            if e.key == pygame.K_DOWN:
                if hero.y < (600-64):
                    hero.y +=1

    """if hero.go_right == True:
        hero.x += 1
        if hero.x > (800-64):
            hero.go_right = False
    else:
        hero.x -= 1"""

    screen.fill((55, 55, 55))
    hero.render()
    zet.render()

    window.blit(screen, (0,0)) #Отображаем screen, (0,0) - начало отрисовки
    pygame.display.flip() # flip - показываем окно
    pygame.time.delay(2) # Вся скорость



