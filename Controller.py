import serial 
import pyautogui 
import pydirectinput
ser = serial.Serial('COM3', 9600) #Enter Arduino Port Number
while True:
    data = ser.readline()
    if data.decode().strip() == "1FE609F": #Enter Forward Hex Values
        pydirectinput.keyDown('w')
        pydirectinput.keyUp('w')

    if data.decode().strip() == "1FEA05F": #Enter Reverse Hex Values
        pydirectinput.keyDown('s')
        pydirectinput.keyUp('s')

    if data.decode().strip() == "1FE40BF": #Enter Left Hexa Values
        pydirectinput.keyDown('a')
        pydirectinput.keyUp('a')

    if data.decode().strip() == "1FEC03F": #Enter Right Hexa Values
        pydirectinput.keyDown('d')
        pydirectinput.keyUp('d')
  

