import unittest

from CalculateGoalPosition import *
from FingersControl import *

class FingersControlTest(unittest.TestCase):

    def testOldMethod(self):
        calc = CalculateGoalPosition(250, 600, 600, 250)
        pos = calc.LeftFinger(0.1)
        control = FingersControl()
        data = control.MoveManage(4, int(pos), 100)
        print(data)


if __name__ == '__main__':
    unittest.main()
