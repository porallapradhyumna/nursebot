import serial
if __name__ == '__main__':
    ser = serial.Serial('COM9', 9600, timeout=1)
    #ser.flush()
    if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
    ser.write(b"forward\n")
    i = 0
    while i<=10:
        i+=1
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
    ser.write(b"stop\n")
            
            
            
            
            
