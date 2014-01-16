from Board import *
from LightRider import *
from Sequence import *

board = Board(GPIO, Board.ALL_LIGHTS, Board.BUTTONS, True)
print board.status()

lr = LightRider(board, True)

seq = Sequence(200, [[1,0,0,0,1,1,1,0,0,1,1,0],[0,1,1,1,0,0,0,1,1,0,0,1]])
lr.addSequence(seq)

lr.run(seq)

print "dne"

