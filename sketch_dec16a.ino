#include <Servo.h>
Servo servo1;
Servo servo2;// create servo object to control a servo
void setup() {
  servo1.attach(9);
  servo2.attach(10);
  servo1.write(0);
  servo2.write(0);
  Serial.begin(9600);// (pin, min, max)
}
char data;
void loop() {
  if(Serial.available()){
    data=Serial.readString()[0];
    switch(data){
      case 'B':servo1.write(90);
      servo2.write(0);
      break;
      case 'N':servo2.write(90);
      servo1.write(0);
      break;
      default:
      servo1.write(0);
      servo2.write(0);
    }
    }
               
}
