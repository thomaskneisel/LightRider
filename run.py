from Board import *
lr = Board(GPIO, Board.ALL_LIGHTS, Board.BUTTONS, True)
print lr.status()

def callMeBack():
	lr.status()

lr.addEventCallback(3, callMeBack)

for led in lr.CHASER_LIGHTS:
	lr.on(led)

print lr.status()

for led in lr.CHASER_LIGHTS:
        lr.off(led)

print lr.status()





