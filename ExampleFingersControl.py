import  time
from FingersControl import *
from CalculateGoalPosition import *

control = FingersControl()
calculate = CalculateGoalPosition(250, 600, 600, 250)

ServoID = 3
ServoID = 4

nullPosLeft = calculate.LeftFinger(0.0)
nullPosRight = calculate.RightFinger(0.0)
fullPosLeft = calculate.LeftFinger(100.0)
fullPosRight = calculate.RightFinger(100.0)

def Move(servo, pos):
    control.MoveManage(servo, int(pos), 100)


#if __name__ == '__main__':
Move(4, nullPosLeft)
time.sleep(1)
Move(3, nullPosRight)
time.sleep(1)
Move(4, fullPosLeft)
time.sleep(1)
Move(3, fullPosRight)
time.sleep(1)





