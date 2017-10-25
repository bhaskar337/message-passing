from config import *

class Signal:

	def __init__(self, on, x, y):
		self.on = on
		self.x = x
		self.y = y

		self.bulb_size = 20
		self.width = 60
		self.height = 120

		self.bulb1_pos = (int(self.x + self.width/2), int(self.y + self.height/4))
		self.bulb2_pos = (int(self.x + self.width/2), int(self.y + 3*self.height/4))


	def switch(self, state):
		self.on = state
		

	def render(self):

		rect = pygame.Rect(self.x, self.y, self.width, self.height)
		pygame.draw.rect(screen, BLACK, rect)

		color1 = GREY if self.on else RED
		color2 = GREEN if self.on else GREY

		pygame.draw.circle(screen, color1, self.bulb1_pos, self.bulb_size)
		pygame.draw.circle(screen, color2, self.bulb2_pos, self.bulb_size)


