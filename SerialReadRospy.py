import rospy
import serial
import numpy as np
from scipy.ndimage import map_coordinates
from matplotlib import pyplot as plt

serialPort = serial.Serial(port = "COM3", baudrate=115200,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serialString = ""                           # Used to hold data coming over UART
arr2D=np.full((8,8),2500)
arr2D[1,1]=0
im=plt.imshow(arr2D,cmap='RdYlBu')
plt.colorbar()
print("Starting \n")

def main():    
    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):
        #print("Printing \n")
        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        #print(serialString,"\n")
        
        #translate the serial message into numpy array
        list1D=[]
        list2D=[]
        for i in range(0,256,32):
            for j in range(0,32,4):
                list1D.append(int(serialString[i+j:i+j+4]))
            list2D.append(list1D)
            list1D=[]
        arr2D=np.array(list2D)
        
        #interpolate to higher resolution
        arr2D=array2D_interpolate(arr2D,32)
        pub.publish()
        #Update Colormesh
        im.set_data(arr2D)
        #print(arr2D)
        plt.pause(0.01)

def array2D_interpolate(array2D,resolution):
        new_size=(resolution,resolution)
        new_dims = []
        for original_length, new_length in zip(arr2D.shape, new_size):
            new_dims.append(np.linspace(0, original_length-1, new_length))
        coords = np.meshgrid(*new_dims, indexing='ij')
        return map_coordinates(array2D,coords)

if __name__ == '__main__':
    pub = rospy.Publisher('tof', String, queue_size=10)
    rospy.init_node('tof_pub', anonymous=True)
    while not rospy.is_shutdown():
        main()
        rospy.spin()