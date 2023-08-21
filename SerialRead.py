import serial

serialPort = serial.Serial(port = "COM3", baudrate=115200,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serialString = ""                           # Used to hold data coming over UART

print("Starting \n")
while(1):
    
    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):
        print("Printimg \n")
        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        #print(serialString.decode('Ascii'))
        print(serialString,"\n")
        print(str(serialString),"\n")
        print(int(serialString[0:4]))
        print(int(serialString[4:8]))
        for i in range(0,224,32):
            for j in range(0,32,4):
                #print(i+j,i+j+4),
                print(int(serialString[i+j:i+j+4]),end =" ")
            print("")
        print("\n")