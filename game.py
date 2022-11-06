# гра
from pygame import *

font.init()
font1 = font.Font(None,35)
lose1 = font.render("Player 1 LOSE", 1, (100,0,0))
#клас батько
class GameSprite(sprite/Sprite):
  def __init__(self, player_image, p_x, p_y, p_speed, width, height):
      super().__init__()
      self.image = transform.scale(image.load(player_image), (width, height))
      self.speed = p_speed
      self.rect = self.image.get_rect()
      self.rect.x = p_x
      self.rect.y = p_y
  def reset(self):
      window.blit(self_image,  (self.rect.x, self.rect.y))
# клас для ракеток 
class Player(GameSprite):
  def update_right(self):
      keys = key.get_pressed()
      if [k_w] and self.rect.y > 5:
        self.rect.y -= self.speed
      if [k_s] and self.rect.y < 420:
        self.rect.y += self.speed
  def update_left(self):
    pass
  
  racket_right = Player("recket_r.png", 520, 200, 4, 50, 150)
  
  ball = GameSprite("ball.png", 200,200,4,50,50)
  win_width = 600
  win_height = 500
  
  window = display.set_mode((win_width, win_height))
  BLue = (200,255,255)
  window.fill(fon)
  
  # прапорці, які відповідають за стан гри
  game = True
  finish = False
  
  clock = time.Clock() #годинник
  FPS = 60 #к-сть кадрів в секунду
  
  #ігровий цикл
  while game:
      for e in event.get(): #перевірка всіх подій
          if e.type == QUIT #тип подій - закрити вікно
              game = False #закінчуємо цикл while
      if finish != True:
          window.fill(fon)
          racket_right.update_right()
          racket_left.update_left()
          ball.rect.x += speed_x
          ball.rect.y += speed_y
          if ball.rect.y
          if ball.rect.y > win_height-50 or ball.rect.y < 0:
              speed_y *= -1
          if sprite.collide_rect(racket_right, ball) or sprite.collide_rect(racket_rect, ball):
              speed_x *= -1
              speed_y *= -1
              #програш лівої ракетки
              if ball.rect.x < 0
              finish = True
              game.over = true
          racket_right.reset()
          racket_left.reset()
          ball.reset()
      display.update()
      clock.tick(FPS)
          
