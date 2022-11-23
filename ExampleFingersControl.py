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
    control.MoveManage(servo, int(nullPos), 100)


if __name__ == '__main__':
    Move(4, nullPosLeft)
    Move(4, fullPosLeft)
    Move(3, nullPosRight)
    Move(3, fullPosRight)





