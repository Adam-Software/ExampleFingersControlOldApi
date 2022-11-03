#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Serial.serialPi import SerialU

class FingersControl():
  def __init__(self):
        super().__init__()
        self.ser = SerialU('/dev/ttyAMA0', 115200)
        
  def servoHandTobytes(self,meseg):
        data = [23]
        d = [meseg[0], meseg[1] >> 8, meseg[1] & 0xff, meseg[2] ]
        data+=d
        data.append(self.CRC8(data[1:]))
        return data

  def CRC8(self, mas):
        st_byt = 0
        crc = 0
        while st_byt < len(mas):
            dat = mas[st_byt]
            for i in range(8):
                fb = crc ^ dat
                fb &= 1
                crc >>= 1
                dat >>= 1
                if fb == 1:
                    crc ^= 0x8c
            st_byt += 1
        return crc

  def MoveManage(self, ServoID, ServoAngl):
     for i in range(2): 
       mes = [ServoID, ServoAngl, 100]
       data = self.servoHandTobytes(mes)
       data.append(36)
            
       self.ser.write(data, len(data))
       return data  
     


