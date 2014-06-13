'''
This python file shall hold my program that places components on a breadboard.

author: Sawyer Vaughan
'''

import pygame

class Model:
	def __init__(self, nodeList):
		self.rows = Rows()
		self.nodeDictionary = nodeList
		self.reorganize_nodes()
		self.nodeLocations = {1: 5}

	def reorganize_nodes(self):
		for i in range(len(self.nodeDictionary)):
			print self.nodeDictionary[i]
			self.nodeDictionary[i] = self.reorganize_list(self.nodeDictionary[i])
			print self.nodeDictionary[i]
		output_list = []
		output_dictionary = {}
		count = 1
		list1 = self.search_for_opamp_node_dictionary()
		output_list.extend(list1)
		list1 = self.search_for_vplus_node_dictionary()
		output_list.extend(list1)
		list1 = self.search_for_ground_node_dictionary()
		output_list.extend(list1)
		list1 = self.search_for_everything_else()
		output_list.extend(list1)
		for entry in output_list:
			output_dictionary[count] = entry
			count += 1
		self.nodeDictionary = output_dictionary

	def reorganize_list(self, input_list):
		output_list = []
		for entry in input_list:
			if isinstance(entry, OpampPin):
				output_list.append(entry)
		for entry in input_list:
			if isinstance(entry, Vplus):
				output_list.append(entry)
		for entry in input_list:
			if isinstance(entry, Ground):
				output_list.append(entry)
		for entry in input_list:
			if isinstance(entry, TwoPin):
				output_list.append(entry)
		return output_list

	def search_for_opamp_node_dictionary(self):
		output_list = []
		for entry in self.nodeDictionary:
			if self.search_list_for_opamp(entry):
				output_list.append(entry)
		return output_list

	def search_for_vplus_node_dictionary(self):
		output_list = []
		for entry in self.nodeDictionary:
			if self.search_list_for_vplus(entry):
				output_list.append(entry)
		return output_list

	def search_for_ground_node_dictionary(self):
		output_list = []
		for entry in self.nodeDictionary:
			if self.search_list_for_ground(entry):
				output_list.append(entry)
		return output_list

	def search_for_everything_else(self):
		output_list = []
		for entry in self.nodeDictionary:
			if self.search_list_for_not_anything(entry):
				output_list.append(entry)
		return output_list

	def search_list_for_opamp(self, input_list):
		for component in input_list:
			if isinstance(component, OpampPin):
				return True
		return False

	def search_list_for_vplus(self, input_list):
		for component in input_list:
			if isinstance(component, OpampPin):
				return False
		for component in input_list:
			if isinstance(component, Vplus):
				return True
		return False

	def search_list_for_ground(self, input_list):
		for component in input_list:
			if isinstance(component, OpampPin):
				return False
		for component in input_list:
			if isinstance(component, Vplus):
				return False
		for component in input_list:
			if isinstance(component, Ground):
				return True
		return False

	def search_list_for_not_anything(self, input_list):
		in1 = self.search_list_for_opamp(input_list)
		in2 = self.search_list_for_vplus(input_list)
		in3 = self.search_list_for_ground(input_list)
		if in1 or in2 or in3:
			return False
		return True

	def place_node(self, nodeNumber):
		pass

	def update_node_dictionary(self):
		pass

	def place_opamp_nodes(self, pin, toprow):
		pass

	def place_component(self):
		pass

class Row:
	def __init__(self, node=None):
		self.node = node

	def add_node(self, node):
		self.node = node

class Rows:
	def __init__(self):
		self.rows1=[]
		for i in range(63):
			self.rows1.append(Row())
		self.rows2=[]
		for i in range(63):
			self.rows2.append(Row())

	def add_node(self, row, side, node):
		if side == 1:
			self.rows1[row].add_node(node)
		if side == 2:
			self.rows2[row].add_node(node)

class Opamp:
	def __init__(self, toprow):
		self.pins = []
		for i in range(14):
			self.pins.append(OpampPin(i))

class OpampPin:
	def __init__(self, pin):
		self.pin = pin

class Vplus:
	def __init__(self):
		pass

class Ground:
	def __init__(self):
		pass

class TwoPin:
	def __init__(self):
		pass

if __name__ == "__main__":
	ground = Ground()
	vplus = Vplus()
	pin = OpampPin(2)
	component = TwoPin()
	model = Model([[pin, component], [component, component], [ground, component], [vplus, component], [component, pin, component, ground]])
	model.rows.add_node(8,2,7)
	print model.rows.rows1[8].node
	print model.rows.rows2[8].node
	print model.nodeDictionary

			