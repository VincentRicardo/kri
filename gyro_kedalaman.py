import sys
sys.path.append('../../')
import time
from DFRobot_BMX160 import BMX160
import math
def calculate_IMU_error():
    c = 0
    AccelZError = 0
    while c < 200:
        data= bmx.get_all_data()
        AccelZ = data[8]
        AccelZError = AccelZError + AccelZ
        c = c+1
    AccelZError = AccelZError / 200    
    print("AccelZError: " + str(AccelZError))
    


bmx = BMX160(1)
currentTime = 0
#begin return True if succeed, otherwise return False
while not bmx.begin():
    time.sleep(2)

def main():
    # kalo mau cek, kommennya ilanging, sisanya di komen
    #calculate_IMU_error()
    previousTime = time.time()
    AccelZ = 0
    Kedalaman = 0 
    while True:
        currentTime = time.time()
        #print(str(currentTime))
        elapsedTime = currentTime - previousTime
        data = bmx.get_all_data()
        AccelZ = data[8]
        Percepatan = AccelZ + 9.283227211440002 #error
        #print("AccelZ = " + str(AccelZ))
        Kedalaman = Kedalaman + ((Percepatan * elapsedTime *elapsedTime)*100)

        print("Kedalaman: " + str(Kedalaman))
        print(" ")
        previousTime = currentTime
    
        

if __name__ == "__main__":
    main()
