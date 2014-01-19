from LightRider.Board import *
from LightRider.LightRider import *
from LightRider.Sequence import *
import sys

board = Board(GPIO, Board.ALL_LIGHTS, Board.BUTTONS, True)
print board.status()

lr = LightRider(board, True)

seq = Sequence(0.2, [[1,1,0,0,0,1,1,1,0,0,1,1,0],[0,1,1,1,0,0,0,1,1,0,0,1]])
lr.addSequence(seq)

lr.run(seq)

print "dne"

