import time
from FingersControl import FingersControl
from calcPosServoHand import calcPosServoHand

pp=FingersControl()
cc=calcPosServoHand()

#
ServoID = 3 

ServoAnglR = 0.00
ServoAnglL = 0.00

HandPos = cc.CalcHand(ServoAnglR,ServoAnglL)

MVManage = pp.MoveManage(ServoID, int(HandPos[0]))

time.sleep(0.02)
#
ServoID = 4 

MVManage = pp.MoveManage(ServoID, int(HandPos[1]))


