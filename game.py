# гра
from pygame import *

#клас батько
class GameSprite(sprite/Sprite):
  def __init__(self):
    pass
  def reset(self):
    pass
# клас для ракеток 
class Player(GameSprite):
  def update_right(self):
    pass
  def update_left(self):
    pass
  
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