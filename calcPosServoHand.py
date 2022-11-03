from ReadHomPos import ReadHomPos

class calcPosServoHand():
    def __init__(self):
        super().__init__()


    def CalcHand(self, GoalPosHandLPer, GoalPosHandRPer):

        ReadPosArray = ReadHomPos()
             
        HandRangeArray = ReadPosArray.ReadServRange()
    
        HandLRangeMin = HandRangeArray[7][0][0]
        HandLRangeMax = HandRangeArray[7][1][0]
        HandRRangeMin = HandRangeArray[7][2][0]
        HandRRangeMax = HandRangeArray[7][3][0]
    
        GoalPosHandL = ((HandLRangeMax - HandLRangeMin) * GoalPosHandLPer) + HandLRangeMin
        GoalPosHandR = ((HandRRangeMax - HandRRangeMin) * GoalPosHandRPer) + HandRRangeMin
     
        return GoalPosHandL, GoalPosHandR

   