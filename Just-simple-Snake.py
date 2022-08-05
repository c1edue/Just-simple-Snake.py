import pygame as pg
import sys
import random
from random import randint
pg.init()
#constants
bk_color = (0, 255, 255)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
block = 20
blocks = 20
marza = 1
color = (0,0,0)
head = 70
snake_color = (0, 204, 0)
head_color = (0, 230, 230)

win_size = [blocks*block+ 2*blocks + marza*blocks,
			blocks*block+ 2*blocks + marza*blocks+head]#game windows size
screen = pg.display.set_mode(win_size)
pg.display.set_caption('Snake')
timer = pg.time.Clock()#fps timer
w = 0
font = pg.font.SysFont('courier', 36)
class SnakeBlock:
	def __init__(self, x ,y):
		self.x = x
		self.y = y

	def snake_fence(self):#check snake in fence
		return 0<=self.x<blocks and 0<=self.y<blocks

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

def blocking(color,ox,oy):#spawn blocks
	pg.draw.rect(screen,color,[blocks+ox*block+marza*(ox+1),
		head+ block +oy*block+marza*(oy+1),
		block,block])

snake_pos=[SnakeBlock(8,9),SnakeBlock(9,9),SnakeBlock(10,9)]#start snake poss

apple = SnakeBlock(2,5)
m_ox = 1#start snake speed
m_oy = 0#start snake speed

while True:#main script

	for event in pg.event.get():
		if event.type == pg.QUIT:
			print('Exit')
			pg.quit()
		elif event.type == pg.KEYDOWN:#game control
			if event.key == pg.K_UP and m_ox!=0:
				m_ox = 0
				m_oy = -1
			elif event.key == pg.K_DOWN and m_ox!=0:
				m_ox = 0
				m_oy = 1
			elif event.key == pg.K_LEFT and m_oy!=0:
				m_ox = -1
				m_oy = 0			
			elif event.key == pg.K_RIGHT and m_oy!=0:
				m_ox = 1
				m_oy = 0
	screen.fill(bk_color)
	pg.draw.rect(screen, head_color,[0,0,win_size[0], head])
	for oy in range(blocks):#crazy background
		for ox in range(blocks):
			w = randint(0,5)
			if w == 1:
				color = (148, 184, 245)
			if w == 2:
				color = (160, 190, 245)
			if w == 3:
				color = (165, 195, 245)
			if w == 4:
				color = (170, 200, 245)
			if w == 5:
				color = (175, 205, 245)
			blocking(color,ox,oy)
	for poss in snake_pos:#snake block
		blocking(snake_color, poss.x, poss.y)

	blocking(red, apple.x, apple.y)

	snake_head = snake_pos[-1]
	if apple == snake_head:#if snake eat MY APPLE!!!!
		snake_pos.append(apple)
		apple = apple_generator()

	if not snake_head.snake_fence():#if snake not in fence you lose:D
		print('LOSE')
		exit()

	def apple_generator():#apple spawn in NO SNAKE!!!11!1!
		x = random.randint(0,blocks-1)
		y = random.randint(0,blocks-1)
		no_snake = SnakeBlock(x,y)

		while no_snake in snake_pos:
			x = random.randint(0,blocks-1)
			y = random.randint(0,blocks-1)
			no_snake = SnakeBlock(x,y)
		return no_snake





	new_snake_head = SnakeBlock(snake_head.x + m_ox, snake_head.y + m_oy)#snake head
	snake_pos.append(new_snake_head)
	snake_pos.pop(0)
	pg.display.flip()
	timer.tick(3)
