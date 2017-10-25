from config import *


class Car:
	def __init__(self, car_type):

		self.speed = 6

		self.width = 80
		self.length = 150
		self.car_type = car_type


		if car_type == 1:
			self.posx = 0
			self.posy = int((WINDOW_HEIGHT - self.width)/2)
			self.car = pygame.image.load('car1.png')
			self.car = pygame.transform.scale(self.car , (self.length, self.width))


		else:
			self.posx = int((WINDOW_WIDTH - self.width)/2)
			self.posy = WINDOW_HEIGHT - self.length
			self.car = pygame.image.load('car2.png')
			self.car = pygame.transform.scale(self.car , (self.width, self.length))


	def render(self):
		screen.blit(self.car, (self.posx, self.posy))


	def move(self, signal):

		if not signal:
			return False

		if self.car_type == 1:
			self.posx += self.speed
			if self.posx >= WINDOW_WIDTH + self.length:
				self.posx = 0
				return True

		else:
			self.posy -= self.speed
			if self.posy <= -self.length:
				self.posy = WINDOW_HEIGHT - self.length
				return True

		return False
