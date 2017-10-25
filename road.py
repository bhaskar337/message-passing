from config import *

class Road:	

	def __init__(self):

		self.width = 100
		self.length = 400

		self.road1_pos = (int((WINDOW_WIDTH - self.length)/2), int((WINDOW_HEIGHT - self.width)/2))
		self.road2_pos = (int((WINDOW_WIDTH - self.width)/2), int((WINDOW_HEIGHT - self.length)/2))


	def render(self):
		rect = pygame.Rect(self.road1_pos + (self.length, self.width))
		pygame.draw.rect(screen, GREY, rect)

		rect = pygame.Rect(self.road2_pos + (self.width, self.length))
		pygame.draw.rect(screen, GREY, rect)

