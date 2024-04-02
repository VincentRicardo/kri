#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver board1 = Adafruit_PWMServoDriver(0x40); 

#define SERVOMIN  125                                                 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  625                                                 // this is the 'maximum' pulse length count (out of 4096)

int sudut[20];
int StringCount = 0;
// void seperate_string(String data) {
//   while (data.length() > 0){
//     int index = data.indexOf(' ');
//     if(index == -1)
//     {
//       sudut[StringCount++] = data;
//       break;
//     }
//     else
//     {
//       sudut[StringCount++] = data.substring(0, index);
//       data = data.substring(index+1);
//     }
//   }
// }

void berdiri(){
  board1.setPWM(0, 0, angleToPulse(60));
  board1.setPWM(1, 0, angleToPulse(105));
  board1.setPWM(2, 0, angleToPulse(180));
  board1.setPWM(3, 0, angleToPulse(65));
  board1.setPWM(4, 0, angleToPulse(70));    
  board1.setPWM(5, 0, angleToPulse(0));
  board1.setPWM(6, 0, angleToPulse(32));
  board1.setPWM(7, 0, angleToPulse(110));
  board1.setPWM(8, 0, angleToPulse(180));
}

void setup() {
  Serial.begin(9600);
  board1.begin();
  board1.setPWMFreq(60);
  berdiri();
}


void loop() 
  { 
    if (Serial.available() > 0){
      String data = Serial.readStringUntil('\n');
      sscanf(data.c_str(), "%d %d %d %d %d %d %d %d %d %d", &sudut[0], &sudut[1], &sudut[2], &sudut[3], &sudut[4], &sudut[5], &sudut[6], &sudut[7], &sudut[8], &sudut[9]);
      if(sudut[0] == 1){
        berdiri();
      }
      else{
        board1.setPWM(1, 0, angleToPulse(170));
        board1.setPWM(4, 0, angleToPulse(10));
        board1.setPWM(7, 0, angleToPulse(180));
        delay(500);
        board1.setPWM(0, 0, angleToPulse(sudut[1]));
        board1.setPWM(3, 0, angleToPulse(sudut[4]));
        board1.setPWM(6, 0, angleToPulse(sudut[7]));

        delay(500);
        board1.setPWM(1, 0, angleToPulse(105));
        board1.setPWM(4, 0, angleToPulse(70));
        board1.setPWM(7, 0, angleToPulse(110));
        delay(500);
        berdiri();
      }      
      //StringCount = 0;

    }
    // board1.setPWM(0, 0, angleToPulse(0));
    // board1.setPWM(1, 0, angleToPulse(180));
    // board1.setPWM(2, 0, angleToPulse(180));
    // board1.setPWM(3, 0, angleToPulse(0));
    // board1.setPWM(4, 0, angleToPulse(0));    
    // board1.setPWM(5, 0, angleToPulse(180));
    //delay(2000);
    
    // board1.setPWM(0, 0, angleToPulse(130));
    // board1.setPWM(1, 0, angleToPulse(180));
    // board1.setPWM(2, 0, angleToPulse(180));
    // board1.setPWM(3, 0, angleToPulse(0));
    // board1.setPWM(4, 0, angleToPulse(0));    
    // board1.setPWM(5, 0, angleToPulse(0));
    // delay(2000);
  }


int angleToPulse(int ang)                             //gets angle in degree and returns the pulse width
  {  int pulse = map(ang,0, 180, SERVOMIN,SERVOMAX);  // map angle of 0 to 180 to Servo min and Servo max 
     return pulse;
  }

