import pygame


class Food:
    def __init__(self, name_image, x, y, width, height):  # конструктор.Создание свойств
        image = pygame.image.load(name_image)  # создание картинки
        self.image = pygame.transform.scale(image, (width, height))

        self.rect = self.image.get_rect()  # создание прям по границам картинки
        self.x = x  # координата х для картинки
        self.y = y  # координата у для картинки

    def draw_image(self):
        screen.blit(self.image, (self.x, self.y))

    def move_food(self):
        self.y += 2

    def move_plate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.x += 3


pygame.init()
window_size = (600, 540)
screen = pygame.display.set_mode(window_size) #создание экрана(окна)
plate = Food('plate.png', 250, 450, 191, 56)
kitchen = Food('kitchen.jpg', 0, 0, 814, 540)

clock = pygame.time.Clock() #создание игровово таймера

while True:  # игрововй таймер
    clock.tick(40)
    kitchen.draw_image()
    plate.draw_image()
    plate.move_plate()
    pygame.display.update()
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            pygame.QUIT()  # выйти из ГОЙДА