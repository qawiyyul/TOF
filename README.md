# VL53L7CX TOF Sensor for Nucleo G4 Board

Should be able to open this project in STM32CubeIDE

I used the document in the link below to setup the registers. Document is meant for F4 Nucleo Board but it works mostly the same for G4 Nucleo Boards.

https://www.st.com/resource/en/user_manual/um3108-how-to-use-stmicroelectronics-xcubetof1-timeofflight-sensor-software-packages-for-stm32cubemx-stmicroelectronics.pdf

Edits are mainly in the TOF/App/app_tof.c file where I marked. It changes the print function from a GUI to a string where the SerialRead.py script can read it.

### SerialRead.py
Required libraries:

```
pip install pyserial numpy scipy matplotlib
```

Reads the serial from the board and turns it into a numpy array. The script also interpolates the numpy array using the scipy library and displays a colour mesh using the matplotlib library. 


### SerialReadRospy.py (incomplete)
This is an attempt to convert the script to a ros node. Have not implemented a way to transmit the numpy array as a ROS message. It can either be implemented using converting the array to prebuilt MultiArray message format or an external library which allows Numpy Array messages. Will also need to be put in a seperate folder to create a package.
