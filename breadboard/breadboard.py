# -*- coding: utf-8 -*-
"""
Created on Mon May  5 20:03:48 2014

@author: sawyer
"""

import pygame
from pygame.locals import *
import time
import pygame.image

size = (400,800)
breadboardSquareWidth = (5,5)
wireWidth = 3

incrementx = size[0]/18
incrementy = size[1]/66


class QuadOpamp:
    def __init__(self, pin_to_nodes={}, toprow=20):
        self.pins = [OpampPin(0, self, toprow, 1), OpampPin(1, self, toprow+1, 1),
        OpampPin(2, self, toprow+2, 1), OpampPin(3, self, toprow+3, 1),
        OpampPin(4, self, toprow+4, 1), OpampPin(5, self, toprow+5, 1),
        OpampPin(6, self, toprow+6, 1), OpampPin(7, self, toprow, 2),
        OpampPin(8, self, toprow+1, 2), OpampPin(9, self, toprow+2, 2),
        OpampPin(10, self, toprow+3, 2), OpampPin(11, self, toprow+4, 2),
        OpampPin(12, self, toprow+5, 2), OpampPin(13, self, toprow+6, 2)]
        self.pin_to_nodes = pin_to_nodes
        
class OpampPin:
    def __init__(self, pinNum, opamp, row, side, connections=[]):
        self.pinNum = pinNum
        self.opamp = opamp
        self.connections = connections
        self.row = row
        self.side = side

class TwoPin:
    def __init__(self, row1, row2, nodes, column, exceptions=[], side=1):
        self.row1 = row1
        self.row2 = row2
        self.nodes = nodes
        self.column = column
        self.minLength = 3
        self.exceptions = exceptions
        self.side = side
        
    def add_exception(self, column):
        self.exceptions.append(column)

class horizontalWire:
    def __init__(self, connection1, connection2, row=None):
        self.connection1 = connection1
        self.connection2 = connection2
        self.row = row
        

class Resistor(TwoPin):
    def __init__(self, resistance, name, nodes, row1=None, row2=None, column=None):
        TwoPin.__init__(self, row1, row2, nodes, column)
        self.resistance = resistance
        self.name = name
        
class Capacitor(TwoPin):
    def __init__(self, capacitance, name, nodes, row1=None, row2=None, column=None):
        TwoPin.__init__(self, row1, row2, nodes, column)
        self.capacitance = capacitance
        self.name = name
        
class Inductor(TwoPin):
    def __init__(self, inductance, name, nodes, row1=None, row2=None, column=None):
        TwoPin.__init__(self, row1, row2, nodes, column)
        self.inductance = inductance
        self.name = name
        
class Vin:
    pass

class Vplus:
    def __init__(self, voltage):
        self.voltage = voltage
        
class Ground:
    def __init__(self):
        self.voltage = 0

class Vminus:
    pass

class Model:
    def __init__(self, rows, nodeDictionary):
        self.rows = rows
        self.nodeDictionary = nodeDictionary
        
    def reorganize_nodes(self):
        outputDict = {}
        count = 1
        keys_to_pop = []
        for key in self.nodeDictionary:
            for component in self.nodeDictionary[key]:
                if isinstance(component, OpampPin):
                    outputDict[count] = self.nodeDictionary[key]
                    count+=1
                    keys_to_pop.append(key)
        for key in keys_to_pop:
            self.nodeDictionary.pop(key)
        keys_to_pop = []
        for key in self.nodeDictionary:
            for component in self.nodeDictionary[key]:
                if isinstance(component, Vplus):
                    outputDict[count] = self.nodeDictionary[key]
                    count+=1
                    keys_to_pop.append(key)
        for key in keys_to_pop:
            self.nodeDictionary.pop(key)
        keys_to_pop = []
        for key in self.nodeDictionary:
            for component in self.nodeDictionary[key]:
                if isinstance(component, Ground):
                    outputDict[count] = self.nodeDictionary[key]
                    count+=1
                    keys_to_pop.append(key)
        for key in keys_to_pop:
            self.nodeDictionary.pop(key)
        for key in self.nodeDictionary:
            outputDict[count] = self.nodeDictionary[key]
            count += 1
        self.nodeDictionary = outputDict
        
    def node_place(self, components, nodeLocations, nodeNumber):
        for component in components:
            if isinstance(component, OpampPin):
                nodeRow = component.row
                self.rows.rows[nodeRow].add_node(nodeNumber)
                for pin in component.opamp.pins:
                    for key in self.nodeDictionary:
                        if pin in nodeDictionary[key]:
                            self.rows.rows[pin.row+63*(pin.side-1)].node = key
                for pin in component.opamp.pins:
                    if self.rows.rows[pin.row+63*(pin.side-1)].node==None:
                        self.rows.rows[pin.row+63*(pin.side-1)].node = 127
                    
        for component in components:
            if isinstance(component, Vplus):
                pass
            if isinstance(component, Ground):
                pass
        for component in components:
            if isinstance(component, TwoPin):
                pass
        return nodeLocations
            
    def draw_horiz_wire(self, pos, startrow=2):
        if pos == 'vplus':
            pass
        if pos == 'mid':
            pass
        if pos == 'ground':
            pass
        
    def place_twopin_down(self, component, startrow=0):
        pass
        
    def place_twopin_up(self, component, startrow=0):
        pass
        
    def place_fourteenpin_down(self, opamp, startrow=0):
        opamp.toprow = startrow
        for i in range(7):
            self.rows.side1
        
        
    def place_twopin_forced(self, component, startrow, endrow):
        if startrow>endrow:
            temp = startrow
            startrow = endrow
            endrow = temp
        component.row1 = startrow
        component.row2 = endrow
            
    def add_occupied(self, component, l):
        pass
    
    def find_unoccupied_column(self, component):
        pass
            
    def add_opamp_connections(component):
        pass

    def add_twopin_connection(self, component):
        pass

class Row:
    def __init__(self, number, side, unoccupied=[0,1,2,3], node=None):
        self.number = number
        self.side = side
        self.unoccupied = unoccupied
        self.node = node
        
    def add_connection(self, component):
        pass
    
    def add_node(node):
        self.node = node
        
    def add_occupied(self, component):
        unoccupied = []
        for entry in self.unoccupied:
            if component != entry:
                unoccupied.append(entry)
        self.unoccupied = unoccupied
    
class Rows:
    def __init__(self):
        self.rows = {}
        count = 0
        for i in range(126):
            if count<63:
                side = 1
            else:
                side = 2
            self.rows[count] = Row(count, side)
            count+=1

class View:
    def __init__(self, screen, model):
        self.screen = screen
        self.model = model
        
    def draw_screen(self):
        for i in range(1, 64):
            for j in range(1, 6):
                pygame.draw.rect(self.screen, (0,0,0), (size[0]/18*(j+3)-breadboardSquareWidth[0]/2, size[1]*(i+1)/66-breadboardSquareWidth[1]/2, breadboardSquareWidth[0], breadboardSquareWidth[1]))
            for j in range(1, 6):
                pygame.draw.rect(self.screen, (0,0,0), (size[0]/18*(j+9)-breadboardSquareWidth[0]/2, size[1]*(i+1)/66-breadboardSquareWidth[1]/2, breadboardSquareWidth[0], breadboardSquareWidth[1]))
        
        for h in range(2):
            for i in range(2):
                for j in range(10):
                    for k in range(5):
                        pygame.draw.rect(self.screen, (0,0,0), (size[0]/18*(15*i+1+h)-breadboardSquareWidth[0]/2, size[1]*(j*6+k+4)/66-breadboardSquareWidth[1]/2, breadboardSquareWidth[0], breadboardSquareWidth[1]))
    
    def node_draw(self, components, row, nodeLocations, nodeNumber):
        for component in components:
            if isinstance(component, TwoPin):
                if nodeNumber == component.nodes[0]:
                    if ('node'+str(component.nodes[1])) not in nodeLocations:
                        self.draw_twopin_down(component, row)
                        endNode = 'node'+str(component.nodes[1])
                        nodeLocations[endNode] = component.row2
                    else:
                        node1 = 'node'+str(component.nodes[0])
                        node2 = 'node'+str(component.nodes[1])
                        self.draw_twopin_forced(component, nodeLocations[node1], nodeLocations[node2])
            if isinstance(component, Vplus):
                self.draw_horiz_wire('vplus', row)
            if isinstance(component, Ground):
                self.draw_horiz_wire('ground', row)
        return nodeLocations
            
    def draw_horiz_wire(self, pos, startrow=2):
        if pos == 'vplus':
            pygame.draw.rect(self.screen, (255,255,0), (size[0]/18, size[1]*(startrow+2)/66-wireWidth/2, size[0]*3/18, wireWidth))
            self.rows.add_occupied(startrow, [0], 1)
            self.rows.add_connection(startrow, Vplus(5), 1)
        if pos == 'mid':
            pygame.draw.rect(self.screen, (80,80,80), (size[0]*8/18, size[1]*(startrow+2)/66-wireWidth/2, size[0]*2/18, wireWidth))
            self.rows.add_occupied(startrow, [4], 1)
            self.rows.add_occupied(startrow, [0], 2)
            self.rows.add_connection(startrow, startrow, 1)
            self.rows.add_connection(startrow, startrow, 2)
        if pos == 'ground':
            pygame.draw.rect(self.screen, (80,80,80), (size[0]*8/18, size[1]*(startrow+2)/66-wireWidth/2, size[0]*2/18, wireWidth))
            pygame.draw.rect(self.screen, (0,0,0), (size[0]*14/18, size[1]*(startrow+2)/66-wireWidth/2, size[0]*3/18, wireWidth))
            self.rows.add_occupied(startrow, [4], 2)
            self.rows.add_connection(startrow, startrow+63, 2)
            
    def draw_vert_thin(self, component, column):
        startrow = component.row1
        endrow = component.row2
        side = component.side
        if isinstance(component, Resistor):
            color = (255,0,0)
        if isinstance(component, Capacitor):
            color = (0,0,255)
        if isinstance(component, Inductor):
            color = (0,255,0)
        if side == 2:
            self.draw_horiz_wire('mid', startrow)
            self.draw_horiz_wire('mid', endrow)
        pygame.draw.rect(self.screen, color, (size[0]*(4+column+6*(side-1))/18-wireWidth/2, size[1]*(startrow+2)/66, wireWidth, size[1]*(endrow-startrow)/66))
        fontObj = pygame.font.Font('freesansbold.ttf', 10)
        msg = component.name
        msgSurfaceObj = fontObj.render(msg, False, (0,0,0))
        msgRectObj = self.screen.get_rect()
        msgRectObj.topleft = (size[0]*(4+column+6*(side-1))/18-15, size[1]*((startrow+endrow)/2+2)/66,)
        self.screen.blit(msgSurfaceObj, msgRectObj)
    
    def draw_horiz_thin(self, component, column):
        if isinstance(component, Resistor):
            color = (255,0,0)
        if isinstance(component, Capacitor):
            color = (0,0,255)
        if isinstance(component, Inductor):
            color = (0,255,0)
        pygame.draw.rect(self.screen, color, (size[0]/18, size[1]*(startrow+2)/66-wireWidth/2, size[0]*3/18, wireWidth))

    def draw_twopin_down(self, component, startrow=0):
        component.row1 = startrow
        running = True
        row=startrow+component.minLength-1
        while running:
            row += 1
            if self.rows.data[row]['connections1'] == []:
                running = False
        component.row2 = row
        column = self.find_unoccupied_column(component, component.side)
        self.rows.add_connection(row, component, component.side)
        self.draw_vert_thin(component, column)
        self.add_connection(component, component.side)
        self.add_occupied(component, [column], component.side)
        
    def draw_fourteenpin_down(self, opamp, startrow=0):
        component.toprow = startrow
        self.add_connection(opamp, component.side)
        self.add_occupied(component, [column], component.side)
        
    def draw_twopin_forced(self, component, startrow, endrow):
        if startrow>endrow:
            temp = startrow
            startrow = endrow
            endrow = temp
        component.row1 = startrow
        component.row2 = endrow
        self.rows.add_connection(startrow, component, 1)
        column = self.find_unoccupied_column(component, component.side)
        self.add_connection(component, component.side)
        self.add_occupied(component, [column], component.side)
        self.draw_vert_thin(component, column)
            
    def add_occupied(self, component, l, side):
        for i in range(component.row1, component.row2+1):
            self.rows.add_occupied(i, l, side)
    
    def find_unoccupied_column(self, component, side):
        thing = 'unoccupied'+str(side)
        for entry in self.rows.data[component.row1][thing]:
            acceptable = True
            for i in range(component.row1, component.row2+1):
                if entry not in self.rows.data[i][thing]:
                    acceptable = False
                if entry in component.exceptions:
                    print 'hey'
                    print component.exceptions
                    print side
                    if entry == 0 and side == 1: 
                        acceptable = False
                    if entry == 4 and side == 2:
                        acceptable = False
                    print acceptable
            if acceptable == True:
                print entry
                return entry
        component.side = 3-component.side
        thing = 'unoccupied'+str(component.side)
        for entry in self.rows.data[component.row1][thing]:
            acceptable = True
            for i in range(component.row1, component.row2+1):
                if entry not in self.rows.data[i][thing]:
                    acceptable = False
                if entry in component.exceptions:
                    if entry == 0 and side == 1: 
                        acceptable = False
                    if entry == 4 and side == 2:
                        acceptable = False
            if acceptable == True:
                return entry
            
    def add_opamp_connections(component):
        pass

    def add_connection(self, component, side):
        self.rows.add_connection(component.row1, component, side)
        self.rows.add_connection(component.row2, component, side)

class Rows:
    def __init__(self, length, columns, nodes={}):
        self.data = {}
        for i in range(length):
            self.data[i] = {'connections1':[], 'connections2':[], 'unoccupied1':range(columns), 'unoccupied2':range(columns)}
        
    def add_connection(self, row, component, side):
        side = 'connections'+str(side)
        self.data[row][side].append(component)
        
    def add_occupied(self, row, l, side):
        side = 'unoccupied'+str(side)
        for entry in l:
            try:
                self.data[row][side].remove(entry)
            except:
                pass
            


def dict_to_picture(d):
    '''d is a dictionary that contains {nodes: [components]}'''
    running = True
    pygame.init()
    pygame.display.set_caption("Breadboard")
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color(255,255,255))
    
    rows = Rows(63, 4)
    model = Model(rows, d)
    view = View(screen, model)
    
    model.reorganize_nodes()    
    print model.nodes
    model.node_place(d, {1:2}, 1)    
    
    nodeLocations = {}
    
    #Running code!:
    
    view.draw_screen()
    
    pygame.display.update()
    
    pygame.image.save(view.screen, 'breadboard.png')
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    
if __name__ == '__main__':
    opamp = QuadOpamp({3:7, 1:4})
    opamp2 = QuadOpamp({2:4, 3:5})
    vplus = Vplus(5)
    R1 = Resistor(10, 'R1', [1,2])
    R2 = Resistor(10, 'R2', [2,4])
    R3 = Resistor(10, 'R3', [1,6])
    R4 = Resistor(10, 'R4', [1,6])
    C1 = Capacitor(10, 'C1', [2,3])
    C2 = Capacitor(10, 'C2', [3,4])
    C3 = Capacitor(10, 'C3', [2,4])
    L1 = Inductor(10, 'L1',[3,5])
    ground = Ground()
    dict_to_picture({1:[R1, R3, R4, ground], 2:[R1, R2, C1, C3], 3:[C1, C2, L1], 4:[ground, R2, C2, R3, C3, opamp2.pins[2]], 5:[vplus, R3, R4], 7:[opamp.pins[3]], 6: [L1, ground, opamp2.pins[3]], 8:[ground, opamp.pins[1]]})
    