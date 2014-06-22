'''
2048 AI implementation 

author: Sawyer and Chris
'''


import pygame, sys
from pygame.locals import *
from random import randint, random
import time
import copy

size = (600,600)

class Tile:
	def __init__(self, row, column, value):
		self.row = row
		self.column = column
		self.value = value

	def get_color(self):
		color = (255,255,255)
		if self.value == 4:
			color = (255,255,255)
		if self.value == 8:
			color = (235,255,255)
		if self.value == 16:
			color = (215,255,255)
		if self.value == 32:
			color = (195,255,255)
		if self.value == 64:
			color = (175,255,255)
		if self.value == 128:
			color = (155,255,255)
		if self.value == 256:
			color = (135,255,255)
		if self.value == 512:
			color = (115,255,255)
		if self.value == 1024:
			color = (95,255,255)
		if self.value == 2048:
			color = (75,255,255)
		if self.value == 4096:
			color = (55,255,255)
		return color

def convert_list_to_tiles(list_of_numbers):
	tiles = []
	for i in range(len(list_of_numbers)):
		if list_of_numbers[i] != 0:
			if i<4:
				row = 1
			elif i<8:
				row = 2
			elif i<12:
				row = 3
			else:
				row = 4
			if i%4 == 0:
				column = 1
			if i%4 == 1:
				column = 2
			if i%4 == 2:
				column = 3
			if i%4 == 3:
				column = 4
			tiles.append(Tile(row,column,list_of_numbers[i]))
	return tiles

class Model:
	def __init__(self, tiles=None):
		if tiles != None:
			self.tiles = tiles
		else:
			self.tiles = []
			self.generate_tile()
			self.generate_tile()

	def get_max_tile(self):
		mx = 0
		for tile in self.tiles:
			if tile.value > mx:
				mx = tile.value
		return mx

	def get_tile_from_position(self, row, column):
		for tile in self.tiles:
			if tile.row == row and tile.column == column:
				return tile
		return None

	def is_valid_move_right(self):
		for i in range(4):
			for j in range(3):
				if self.get_tile_from_position(i+1, j+1) != None and self.get_tile_from_position(i+1, j+2) == None: #get tile to the right, valid if there is a blank space next to tile
					return True
				if self.get_tile_from_position(i+1, j+1) != None and self.get_tile_from_position(i+1, j+2) != None: #get tile next to, valid if they're equal
					if self.get_tile_from_position(i+1, j+1).value == self.get_tile_from_position(i+1, j+2).value:
						return True
		return False

	def is_valid_move_left(self):
		for i in range(4):
			for j in range(3):
				if self.get_tile_from_position(i+1, 4-j) != None and self.get_tile_from_position(i+1, 3-j) == None: #get tile to the right, valid if there is a blank space next to tile
					return True
				if self.get_tile_from_position(i+1, 4-j) != None and self.get_tile_from_position(i+1, 3-j) != None: #get tile next to, valid if they're equal
					if self.get_tile_from_position(i+1, 4-j).value == self.get_tile_from_position(i+1, 3-j).value:
						return True
		return False

	def is_valid_move_up(self):
		for i in range(4):
			for j in range(3):
				if self.get_tile_from_position(4-j, i+1) != None and self.get_tile_from_position(3-j, i+1) == None: #get tile to the right, valid if there is a blank space next to tile
					return True
				if self.get_tile_from_position(4-j, i+1) != None and self.get_tile_from_position(3-j, i+1) != None: #get tile next to, valid if they're equal
					if self.get_tile_from_position(4-j, i+1).value == self.get_tile_from_position(3-j, i+1).value:
						return True
		return False

	def is_valid_move_down(self):
		for i in range(4):
			for j in range(3):
				if self.get_tile_from_position(j+1, i+1) != None and self.get_tile_from_position(j+2, i+1) == None: #get tile to the right, valid if there is a blank space next to tile
					return True
				if self.get_tile_from_position(j+1, i+1) != None and self.get_tile_from_position(j+2, i+1) != None: #get tile next to, valid if they're equal
					if self.get_tile_from_position(j+1, i+1).value == self.get_tile_from_position(j+2, i+1).value:
						return True
		return False

	def row_collapse_left_or_up(self, list_of_numbers):
		new_list = []
		length = len(list_of_numbers)
		if length==1:
			return list_of_numbers
		for i in range(len(list_of_numbers)):
			if i == length-1:
				new_list.append(list_of_numbers[i])
			elif list_of_numbers[i]==list_of_numbers[i+1]:
				new_list.append(list_of_numbers[i]*2)
				new_list.extend(self.row_collapse_left_or_up(list_of_numbers[i+2:]))
				break
			else:
				new_list.append(list_of_numbers[i])
		return new_list

	def row_collapse_right_or_down(self, list_of_numbers):
		temp_list = []
		length = len(list_of_numbers)
		for i in range(len(list_of_numbers)):
			temp_list.append(list_of_numbers[length-i-1])
		list_of_numbers = temp_list
		new_list = []
		length = len(list_of_numbers)
		if length==1:
			return list_of_numbers
		for i in range(len(list_of_numbers)):
			if i == length-1:
				new_list.append(list_of_numbers[i])
			elif list_of_numbers[i]==list_of_numbers[i+1]:
				new_list.append(list_of_numbers[i]*2)
				new_list.extend(self.row_collapse_right_or_down(list_of_numbers[i+2:]))
				break
			else:
				new_list.append(list_of_numbers[i])
		return new_list

	def get_row_tile_values(self, row):
		tile_values = []
		tiles = []
		for tile in self.tiles:
			if tile.row == row:
				tiles.append(tile)
		for tile in tiles:
			if tile.column == 1:
				tile_values.append(tile.value)
		for tile in tiles:
			if tile.column == 2:
				tile_values.append(tile.value)
		for tile in tiles:
			if tile.column == 3:
				tile_values.append(tile.value)
		for tile in tiles:
			if tile.column == 4:
				tile_values.append(tile.value)
		return tile_values

	def get_column_tile_values(self, column):
		tile_values = []
		tiles = []
		for tile in self.tiles:
			if tile.column == column:
				tiles.append(tile)
		for tile in tiles:
			if tile.row == 1:
				tile_values.append(tile.value)
		for tile in tiles:
			if tile.row == 2:
				tile_values.append(tile.value)
		for tile in tiles:
			if tile.row == 3:
				tile_values.append(tile.value)
		for tile in tiles:
			if tile.row == 4:
				tile_values.append(tile.value)
		return tile_values

	def generate_tile(self):
		row = randint(1,4)
		column = randint(1,4)
		if random() < .9:
			value = 2
		else:
			value = 4
		if self.get_tile_from_position(row, column) != None:
			self.generate_tile()
		else:
			self.add_tile(row,column,value)

	def add_tile(self,row,column,value):
		self.tiles.append(Tile(row,column,value))

	def update_left(self):
		if self.is_valid_move_left():
			new_tiles = []
			for i in range(4):
				values = self.get_row_tile_values(i+1)
				new_values = self.row_collapse_left_or_up(values)
				column = 1
				for j in range(len(new_values)):
					new_tiles.append(Tile(i+1, column, new_values[j]))
					column+=1
			self.tiles = new_tiles

	def update_up(self):
		if self.is_valid_move_up():
			new_tiles = []
			for i in range(4):
				values = self.get_column_tile_values(i+1)
				new_values = self.row_collapse_left_or_up(values)
				row = 1
				for j in range(len(new_values)):
					new_tiles.append(Tile(row, i+1, new_values[j]))
					row+=1
			self.tiles = new_tiles

	def update_right(self):
		if self.is_valid_move_right():
			new_tiles = []
			for i in range(4):
				values = self.get_row_tile_values(i+1)
				new_values = self.row_collapse_right_or_down(values)
				column = 4
				for j in range(len(new_values)):
					new_tiles.append(Tile(i+1, column, new_values[j]))
					column-=1
			self.tiles = new_tiles

	def update_down(self):
		if self.is_valid_move_down():
			new_tiles = []
			for i in range(4):
				values = self.get_column_tile_values(i+1)
				new_values = self.row_collapse_right_or_down(values)
				row = 4
				for j in range(len(new_values)):
					new_tiles.append(Tile(row, i+1, new_values[j]))
					row-=1
			self.tiles = new_tiles

class View:
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill((0,0,0))
        self.draw_tiles()
        pygame.display.update()

    def draw_tiles(self):
    	for tile in self.model.tiles:
    		self.draw_square(tile)
    		self.draw_tile(tile)

    def draw_square(self, tile):
    	color = tile.get_color()
        pos = (size[0]/4.0*(tile.column-1), size[1]/4.0*(tile.row-1))
        pygame.draw.rect(self.screen, color, (pos[0], pos[1], size[0]/4.0, size[1]/4.0))

    def draw_tile(self, tile):
    	color = tile.get_color()
    	pos = (size[0]/4.0*(tile.column-1), size[1]/4.0*(tile.row-1))
    	fontObj = pygame.font.Font('freesansbold.ttf', 32)
    	msg = str(tile.value)
    	msgSurfaceObj = fontObj.render(msg, False, (0,0,0))
    	msgRectObj = self.screen.get_rect()
    	msgRectObj.topleft = pos
    	screen.blit(msgSurfaceObj, msgRectObj)

class Controller:
	def __init__(self, model):
		self.model = model

	def get_valid_moves(self, model):
		moves = []
		if model.is_valid_move_up():
			moves.append('up')
		if model.is_valid_move_down():
			moves.append('down')
		if model.is_valid_move_right():
			moves.append('right')
		if model.is_valid_move_left():
			moves.append('left')
		return moves

	def handle_pygame_event(self, event):
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP:
                	if 'up' in self.get_valid_moves(self.model):
	                    self.model.update_up()
	                    self.model.generate_tile()
                if event.key == pygame.K_DOWN:
                	if 'down' in self.get_valid_moves(self.model):
	                    self.model.update_down()
	                    self.model.generate_tile()
                if event.key == pygame.K_RIGHT:
                	if 'right' in self.get_valid_moves(self.model):
	                    self.model.update_right()
	                    self.model.generate_tile()
                if event.key == pygame.K_LEFT:
                	if 'left' in self.get_valid_moves(self.model):
		                self.model.update_left()
		                self.model.generate_tile()


class AIcontroller:
	def __init__(self, model):
		self.model = model

	def move(self):
		scoreWeights = {1:1.1, 2:1, 3:.5, 4:.2}
		scores = {}
		valid_directions = self.get_valid_moves(self.model)
		for direction in valid_directions:
			scores[direction] = 0
		for depth in scoreWeights:
			modelDict = self.make_all_child_nodes(self.model,depth,depth)
			scoreDict = self.convert_dictionary_of_models_to_scores(modelDict)
			scores_for_certain_depth = self.flatten_dictionary_of_scores(scoreDict)
			for key in scores_for_certain_depth:
				scores[key] += scoreWeights[depth]*scores_for_certain_depth[key]
		direction = self.find_max_dictionary_value(scores)
		if direction in self.get_valid_moves(self.model):
			if direction == 'up':
				self.model.update_up()
				self.model.generate_tile()
			if direction == 'down':
				self.model.update_down()
				self.model.generate_tile()
			if direction == 'right':
				self.model.update_right()
				self.model.generate_tile()
			if direction == 'left':
				self.model.update_left()
				self.model.generate_tile()

	def get_valid_moves(self, model):
		moves = []
		if model.is_valid_move_up():
			moves.append('up')
		if model.is_valid_move_down():
			moves.append('down')
		if model.is_valid_move_right():
			moves.append('right')
		if model.is_valid_move_left():
			moves.append('left')
		return moves

	def get_tiles_without_move(self):
		for tile in self.model.tiles:
			tileRight = self.get_tile_from_position(tile.row+1, tile.column+1)

	def make_model_copy(self, direction, input_model):
		model = copy.deepcopy(input_model)
		if direction == 'right':
			model.update_right()
		if direction == 'down':
			model.update_down()
		if direction == 'up':
			model.update_up()
		if direction == 'left':
			model.update_left()
		return model

	def make_all_child_nodes(self, model, depth, max_depth):
		directions = ['left','right','up','down']
		if max_depth == 1:
			output = {}
			for direction in directions:
				if direction in self.get_valid_moves(model):
					output[direction] = [self.make_model_copy(direction, model)]
			return output
		if depth == 1:
			output = []
			for direction in directions:
				if direction in self.get_valid_moves(model):
					output.append(self.make_model_copy(direction, model))
			return output
		if depth == max_depth:
			output = {}
			for direction in directions:
				if direction in self.get_valid_moves(model):
					new_model = self.make_model_copy(direction, model)
					output[direction] = self.make_all_child_nodes(new_model, depth-1, max_depth)
			return output
		output = []
		for direction in directions:
			if direction in self.get_valid_moves(model):
				new_model = self.make_model_copy(direction, model)
				output.append(self.make_all_child_nodes(new_model, depth-1, max_depth))
		return output

	def convert_dictionary_of_models_to_scores(self, dictionary):
		if isinstance(dictionary, dict):
			output = {}
			for key in dictionary:
				output[key] = self.convert_dictionary_of_models_to_scores(dictionary[key])
			return output
		if isinstance(dictionary, list):
			output = []
			for entry in dictionary:
				output.append(self.convert_dictionary_of_models_to_scores(entry))
			return output
		if isinstance(dictionary, Model):
			return self.board_evaluation_function(dictionary)

	def flatten_dictionary_of_scores(self,dictionary):
		if isinstance(dictionary, dict):
			output = {}
			for key in dictionary:
				output[key] = self.flatten_dictionary_of_scores(dictionary[key])
				output[key] += self.board_evaluation_function(self.make_model_copy(key, self.model))
			return output
		if not isinstance(dictionary[0], list):
			return max(dictionary)
		output = []
		for entry in dictionary:
			output.append(self.flatten_dictionary_of_scores(entry))
		return max(output)

	def return_child_node_scores(self, depth, max_depth, input_model):
		directions = ['left','right','up','down']
		if depth == max_depth:
			output = {}
			for direction in directions:
				model = self.make_model_copy(direction, input_model)
				output[direction] = self.return_child_node_scores(depth-1, max_depth, model)
				output[direction] += self.board_evaluation_function(input_model)
			return output
		if depth == 0: 
			return self.board_evaluation_function_high_depth(input_model)
		output = []
		for direction in directions:
			model = self.make_model_copy(direction, input_model)
			output.append(self.return_child_node_scores(depth-1, max_depth, model))
		return output

	def board_evaluation_function(self, model):
		score = 0
		if model.get_tile_from_position(1,1) != None:
			score += model.get_tile_from_position(1,1).value
		if model.get_tile_from_position(1,2) != None:
			score += model.get_tile_from_position(1,2).value/2.0
		if model.get_tile_from_position(1,3) != None:
			score += model.get_tile_from_position(1,3).value/4.0
		if model.get_tile_from_position(1,4) != None:
			score += model.get_tile_from_position(1,4).value/8.0
		k=self.model.get_max_tile()/30.0
		score -= k*len(model.tiles)
		return score

	def board_evaluation_function_high_depth(self, model):
		k=1
		return -k*len(model.tiles)

	def find_max_dictionary_value(self, dictionary):
		value = -10000000
		max_key = None
		for key in dictionary:
			if dictionary[key]>value:
				max_key = key
				value = dictionary[key]
			if dictionary[key] == value:
				max_key = self.pick_better_key(max_key, key)
		return max_key

	def pick_better_key(self, key1, key2):
		if key1 == 'up' or key2 == 'up':
			return 'up'
		if key1 == 'left' or key2 == 'left':
			return 'left'
		if key1 == 'right' or key2 == 'right':
			return 'right'
		if key1 == 'down' or key2 == 'down':
			return 'down'

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("2048 AI")
    screen = pygame.display.set_mode(size)

    x = convert_list_to_tiles([2,2,0,2,2,2,2,0,2,0,2,0,4,2,4])
    model = Model() 
    view = View(model, screen)
    controller = AIcontroller(model)
    view.draw()

    if isinstance(controller, Controller):
	    while True:
	        for event in pygame.event.get():
	            if  event.type == QUIT:
	                pygame.quit()
	                sys.exit()
	            controller.handle_pygame_event(event)
	            view.draw()
	        pygame.display.update()

    if isinstance(controller, AIcontroller):
		while True:
			for event in pygame.event.get():
				if  event.type == QUIT:
					pygame.quit()
					sys.exit()
			controller.move()
			view.draw()
			pygame.display.update()
