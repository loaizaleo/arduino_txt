import serial

serialport = serial.Serial("/dev/ttyACM0",baudrate=9600, timeout=120)
textfile = open("pulsor_sensor.dat","w")
for i in range(0,1200):
    arduinodata=serialport.readline().decode("ascii")
    print(arduinodata)
    textfile.write(arduinodata)
textfile.close()
