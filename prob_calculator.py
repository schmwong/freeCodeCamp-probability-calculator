import copy
import random
# Consider using the modules imported above.

class Hat:

	def __init__(self, **kwargs):
		self.inventory = {}
		self.contents = []

		# Save a copy of the kwargs dictionary,
		# at the same time making sure the numbers are int and not str
		for colour, quantity in kwargs.items():
			self.inventory[colour] = int(quantity)

		# For each colour (dictionary key),
			# for as many times as indicated (corresponding value),
				# add the colour name to the list
		for colour in self.inventory:
			for ball in range(self.inventory[colour]):
				self.contents.append(colour)


	def draw(self, num_to_draw):
		# Draw all the balls from the hat at most, not more
		num_to_draw = min(num_to_draw, len(self.contents))
		
		drawn = random.sample(self.contents, num_to_draw)
		for ball in drawn:
			self.contents.remove(ball)
		
		return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

	M = 0
	hit = 0
	missed = 0
	
	for round in range(num_experiments):
		# Make a new copy of the hat for each round
		active_hat = copy.deepcopy(hat)
		
		# Call the draw method; returns list of drawn balls
		drawn = active_hat.draw(num_balls_drawn)

		# Populate wishlist in the same way 
		# that was done for the hat contents attribute
		wishlist = []
		for colour in expected_balls:
			for ball in range(expected_balls[colour]):
				wishlist.append(colour)

		# Check off items in wishlist that appear in drawn list
		for ball in drawn:
			try:
				wishlist.remove(ball)
				hit += 1
			except:
				missed += 1

		# Add 1 to success count if all wishlist items are checked off
		if len(wishlist) == 0:
			M += 1

	probability = M / num_experiments
	
	print(f"Hit: {hit}, Missed: {missed}, Total: {hit + missed}")
	print(f"Hit Rate: {hit / (hit + missed) * 100}%")
	print(f"Probability: {probability}")

	return probability
		