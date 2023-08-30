# VL53L7CX TOF Sensor for Nucleo G4 Board
Edits are mainly in the TOF/App/app_tof.c file where I marked. It changes the print function from a GUI to a string where the SerialRead.py script can read it.

### Setup (for Windows)
Ensure STM32CubeIDE is installed on your computer.

https://www.st.com/en/development-tools/stm32cubeide.html

Download the zip file for this repository and extract it to your desired workspace.(Or if you have Git you can clone it)

Open the TOF-main folder and open the .project file to open the project in STM32CubeIDE

Attach the STM32 G4 Nucleo board via USB and upload the code by pressing the run debug button

![attached board](/readmeimages/image.png "attached board")
![upload button](/readmeimages/image.png "upload button")

### SerialRead.py
Reads the serial from the board and turns it into a numpy array. The script also interpolates the numpy array using the scipy library and displays a colour mesh using the matplotlib library. 

#### Setup

```
pip install pyserial numpy scipy matplotlib
```
Ensure code has been uploaded to the board and attach board to PC

Run SerialRead.py in terminal
```
python SerialRead.py
```
![program output](/readmeimages/image.png "program output")

ctrl-c in the terminal to shut down the program

### If you need to redo the whole project,

I used the document in the link below to setup the registers. Document is meant for F4 Nucleo Board but it works mostly the same for G4 Nucleo Boards.

https://www.st.com/resource/en/user_manual/um3108-how-to-use-stmicroelectronics-xcubetof1-timeofflight-sensor-software-packages-for-stm32cubemx-stmicroelectronics.pdf

### SerialReadRospy.py (incomplete)
This is an attempt to convert the script to a ros node. Have not implemented a way to transmit the numpy array as a ROS message. It can either be implemented using converting the array to prebuilt MultiArray message format or an external library which allows Numpy Array messages. Will also need to be put in a seperate folder to create a package.
