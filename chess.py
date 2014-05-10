# -*- coding: utf-8 -*-
"""
Created on Mon May  5 20:23:59 2014

@author: sawyer
"""

all_spaces = []
for i in range(1,9):
    for j in range(1,9):
        all_spaces.append((i,j))

class Piece():
    def __init__(self, pos, team):
        self.pos = pos
        self.team = team
        self.alive = True
        
    def move(self, end_pos):
        self.pos = end_pos
        
    def check_valid_moves(self, moves):
        valid_moves = []
        for move in moves:
            if move[0] in range(1,9) and move[1] in range(1,9):
                valid_moves.append(move)
        return valid_moves

class Pawn(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
        
    def valid_moves(self, white_spaces, black_spaces):
        moves = []
        if self.team == 'Black':
            if (self.pos[0]+1, self.pos[1]) not in black_spaces:
                if (self.pos[0]+1, self.pos[1]) not in white_spaces:
                    moves.append((self.pos[0]+1, self.pos[1]))
                    if (self.pos[0]+1, self.pos[1]) not in white_spaces:
                        if (self.pos[0]+2, self.pos[1]) not in black_spaces:
                            if (self.pos[0]+2, self.pos[1]) not in white_spaces:
                                moves.append((self.pos[0]+2, self.pos[1]))
            if (self.pos[0]+1, self.pos[1]+1) in white_spaces:
                moves.append((self.pos[0]+1, self.pos[1]+1))
            if (self.pos[0]+1, self.pos[1]-1) in white_spaces:
                moves.append((self.pos[0]+1, self.pos[1]-1))
            self.check_valid_moves(moves)
            return moves
        if self.team == 'White':
            if (self.pos[0]-1, self.pos[1]) not in black_spaces:
                if (self.pos[0]-1, self.pos[1]) not in white_spaces:
                    moves.append((self.pos[0]-1, self.pos[1]))
                    if (self.pos[0]-1, self.pos[1]) not in black_spaces:
                        if (self.pos[0]-2, self.pos[1]) not in white_spaces:
                            if (self.pos[0]-2, self.pos[1]) not in black_spaces:
                                moves.append((self.pos[0]-2, self.pos[1]))
            if (self.pos[0]-1, self.pos[1]+1) in black_spaces:
                moves.append((self.pos[0]-1, self.pos[1]+1))
            if (self.pos[0]-1, self.pos[1]-1) in black_spaces:
                moves.append((self.pos[0]-1, self.pos[1]-1))
            moves = self.check_valid_moves(moves)
            return moves
    
class Rook(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
        
    def valid_moves(self, white_spaces, black_spaces):
        moves = []
        directions = ['right', 'left', 'up', 'down']
        for direction in directions:
            print direction
            if direction == 'right':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>7:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0], self.pos[1]+count) not in white_spaces:
                            moves.append((self.pos[0], self.pos[1]+count))
                            if (self.pos[0], self.pos[1]+count) in black_spaces:
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0], self.pos[1]+count) not in black_spaces:
                            moves.append((self.pos[0], self.pos[1]+count))
                            if (self.pos[0], self.pos[1]+count) in white_spaces:
                                run = False
                        else: 
                            run = False
            if direction == 'left':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>7:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0], self.pos[1]-count) not in white_spaces:
                            moves.append((self.pos[0], self.pos[1]-count))
                            if (self.pos[0], self.pos[1]-count) in black_spaces:
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0], self.pos[1]-count) not in black_spaces:
                            moves.append((self.pos[0], self.pos[1]-count))
                            if (self.pos[0], self.pos[1]-count) in white_spaces:
                                run = False
                        else: 
                            run = False
            if direction == 'up':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>7:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]-count, self.pos[1]) not in white_spaces:
                            moves.append((self.pos[0]-count, self.pos[1]))
                            if (self.pos[0]-count, self.pos[1]) in black_spaces:
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]-count, self.pos[1]) not in black_spaces:
                            moves.append((self.pos[0]-count, self.pos[1]))
                            if (self.pos[0]-count, self.pos[1]) in white_spaces:
                                run = False
                        else: 
                            run = False
            if direction == 'down':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>7:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]+count, self.pos[1]) not in white_spaces:
                            moves.append((self.pos[0]+count, self.pos[1]))
                            if (self.pos[0]+count, self.pos[1]) in black_spaces:
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]+count, self.pos[1]) not in black_spaces:
                            moves.append((self.pos[0]+count, self.pos[1]))
                            if (self.pos[0]+count, self.pos[1]) in white_spaces:
                                run = False
                        else: 
                            run = False
        moves = self.check_valid_moves(moves)
        return moves
                            
                            
    
class Bishop(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
        
    def valid_moves(self, white_spaces, black_spaces):
        moves = []
        directions = ['right', 'left', 'up', 'down']
        for direction in directions:
            print direction
            if direction == 'right':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>7:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]+count, self.pos[1]+count) not in white_spaces:
                            moves.append((self.pos[0]+count, self.pos[1]+count))
                            if (self.pos[0]+count, self.pos[1]+count) in black_spaces:
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]+count, self.pos[1]+count) not in black_spaces:
                            moves.append((self.pos[0]+count, self.pos[1]+count))
                            if (self.pos[0]+count, self.pos[1]+count) in white_spaces:
                                run = False
                        else: 
                            run = False
            if direction == 'left':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>7:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]+count, self.pos[1]-count) not in white_spaces:
                            moves.append((self.pos[0]+count, self.pos[1]-count))
                            if (self.pos[0]+count, self.pos[1]-count) in black_spaces:
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]+count, self.pos[1]-count) not in black_spaces:
                            moves.append((self.pos[0]+count, self.pos[1]-count))
                            if (self.pos[0]+count, self.pos[1]-count) in white_spaces:
                                run = False
                        else: 
                            run = False
            if direction == 'up':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>7:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]-count, self.pos[1]+count) not in white_spaces:
                            moves.append((self.pos[0]-count, self.pos[1]+count))
                            if (self.pos[0]-count, self.pos[1]+count) in black_spaces:
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]-count, self.pos[1]+count) not in black_spaces:
                            moves.append((self.pos[0]-count, self.pos[1]+count))
                            if (self.pos[0]-count, self.pos[1]+count) in white_spaces:
                                run = False
                        else: 
                            run = False
            if direction == 'down':
                run = True
                count = 0
                while run:
                    count+=1
                    if count>7:
                        run = False
                    if self.team == 'White':
                        if (self.pos[0]-count, self.pos[1]-count) not in white_spaces:
                            moves.append((self.pos[0]-count, self.pos[1]-count))
                            if (self.pos[0]-count, self.pos[1]-count) in black_spaces:
                                run = False
                        else: 
                            run = False
                    if self.team == 'Black':
                        if (self.pos[0]-count, self.pos[1]-count) not in black_spaces:
                            moves.append((self.pos[0]-count, self.pos[1]-count))
                            if (self.pos[0]-count, self.pos[1]-count) in white_spaces:
                                run = False
                        else: 
                            run = False
        moves = self.check_valid_moves(moves)
        return moves
    
class Knight(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
        
    def valid_moves(self, white_spaces, black_spaces):
        if self.team == 'White':
            if (self.pos[0]-2, self.pos[1]-1) not in white_spaces:
                moves.append((self.pos[0]-2, self.pos[1]-1))
        if self.team == 'White':
            if (self.pos[0]-2, self.pos[1]+1) not in white_spaces:
                moves.append((self.pos[0]-2, self.pos[1]+1))
        if self.team == 'White':
            if (self.pos[0]-1, self.pos[1]-2) not in white_spaces:
                moves.append((self.pos[0]-1, self.pos[1]-2))
        if self.team == 'White':
            if (self.pos[0]-1, self.pos[1]+2) not in white_spaces:
                moves.append((self.pos[0]-1, self.pos[1]+2))
        if self.team == 'White':
            if (self.pos[0]+1, self.pos[1]-2) not in white_spaces:
                moves.append((self.pos[0]+1, self.pos[1]-2))
        if self.team == 'White':
            if (self.pos[0]+1, self.pos[1]+2) not in white_spaces:
                moves.append((self.pos[0]+1, self.pos[1]+2))
        if self.team == 'White':
            if (self.pos[0]+2, self.pos[1]-1) not in white_spaces:
                moves.append((self.pos[0]+2, self.pos[1]-1))
        if self.team == 'White':
            if (self.pos[0]+2, self.pos[1]+1) not in white_spaces:
                moves.append((self.pos[0]+2, self.pos[1]+1))
        if self.team == 'Black':
            if (self.pos[0]-2, self.pos[1]-1) not in black_spaces:
                moves.append((self.pos[0]-2, self.pos[1]-1))
        if self.team == 'Black':
            if (self.pos[0]-2, self.pos[1]+1) not in black_spaces:
                moves.append((self.pos[0]-2, self.pos[1]+1))
        if self.team == 'Black':
            if (self.pos[0]-1, self.pos[1]-2) not in black_spaces:
                moves.append((self.pos[0]-1, self.pos[1]-2))
        if self.team == 'Black':
            if (self.pos[0]-1, self.pos[1]+2) not in black_spaces:
                moves.append((self.pos[0]-1, self.pos[1]+2))
        if self.team == 'Black':
            if (self.pos[0]+1, self.pos[1]-2) not in black_spaces:
                moves.append((self.pos[0]+1, self.pos[1]-2))
        if self.team == 'Black':
            if (self.pos[0]+1, self.pos[1]+2) not in black_spaces:
                moves.append((self.pos[0]+1, self.pos[1]+2))
        if self.team == 'Black':
            if (self.pos[0]+2, self.pos[1]-1) not in black_spaces:
                moves.append((self.pos[0]+2, self.pos[1]-1))
        if self.team == 'Black':
            if (self.pos[0]+2, self.pos[1]+1) not in black_spaces:
                moves.append((self.pos[0]+2, self.pos[1]+1))
    
class King(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
    
class Queen(Piece):
    def __init__(self, pos, team):
        Piece.__init__(self, pos, team)
        
class Pieces:
    def __init__(self):
        self.wp1 = Pawn((7,1), 'White')
        self.wp2 = Pawn((7,2), 'White')
        self.wp3 = Pawn((7,3), 'White')
        self.wp4 = Pawn((7,4), 'White')
        self.wp5 = Pawn((7,5), 'White')
        self.wp6 = Pawn((7,6), 'White')
        self.wp7 = Pawn((7,7), 'White')
        self.wp8 = Pawn((7,8), 'White')
        self.wr1 = Rook((8,1), 'White')
        self.wk1 = Knight((8,2), 'White')
        self.wb1 = Bishop((8,3), 'White')
        self.wq = Queen((8,4), 'White')
        self.wk = King((8,5), 'White')
        self.wb2 = Bishop((8,6), 'White')
        self.wk2 = Knight((8,7), 'White')
        self.wr2 = Rook((8,8), 'White')
        self.bp1 = Pawn((2,1), 'Black')
        self.bp2 = Pawn((2,2), 'Black')
        self.bp3 = Pawn((2,3), 'Black')
        self.bp4 = Pawn((2,4), 'Black')
        self.bp5 = Pawn((2,5), 'Black')
        self.bp6 = Pawn((2,6), 'Black')
        self.bp7 = Pawn((2,7), 'Black')
        self.bp8 = Pawn((2,8), 'Black')
        self.br1 = Rook((1,1), 'Black')
        self.bk1 = Knight((1,2), 'Black')
        self.bb1 = Bishop((1,3), 'Black')
        self.bq= Queen((1,4), 'Black')
        self.bk = King((1,5), 'Black')
        self.bb2 = Bishop((1,6), 'Black')
        self.bk2 = Knight((1,7), 'Black')
        self.br2 = Rook((1,8), 'Black')
        self.pieces = [self.wp1, self.wp2, self.wp3, self.wp4, self.wp5, 
                       self.wp6, self.wp7, self.wp8, self.wr1, self.wb1, 
                       self.wk1, self.wk, self.wq, self.wb2, self.wk2, self.wr2,
                       self.bp1, self.bp2, self.bp3, self.bp4, self.bp5, self.bp6,
                       self.bp7, self.bp8, self.br1, self.bk1, self.bb1, self.bq,
                       self.bk, self.bb2, self.bk2, self.br2]
                       

    def get_white_spaces(self):
        spaces = []
        for piece in self.pieces:
            if piece.team == 'White':
                spaces.append(piece.pos)
        return spaces
    
    def get_black_spaces(self):
        spaces = []
        for piece in self.pieces:
            if piece.team == 'Black':
                spaces.append(piece.pos)
        return spaces
        
class Model:
    pass

class View:
    pass

class Controller:
    pass

if __name__ == "__main__":
    pieces = Pieces()
    pieces.bb2.move((4,4))
    print pieces.bb2.pos
    print pieces.bb2.valid_moves(pieces.get_white_spaces(), pieces.get_black_spaces())
        