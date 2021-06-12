#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define MIN_PULSE_WIDTH 650
#define MAX_PULSE_WIDTH 2350
#define DEFAULT_PULSE_WIDTH 1500
#define FREQUENCY 50

uint8_t servonum = 0;
int count;
int count1;
int incoming;
void setup() 
{
Serial.begin(115200);
Serial.setTimeout(1);
//Serial.println("16 channel Servo test!");
count = 90;
count1 = 90;
pwm.begin();
pwm.setPWMFreq(FREQUENCY);
pwm.setPWM(0, 0, pulseWidth(count));
pwm.setPWM(1, 0, pulseWidth(count1));
}
int pulseWidth(int angle)
{
int pulse_wide, analog_value;
pulse_wide = map(angle, 0, 180, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
analog_value = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
//Serial.println(analog_value);
return analog_value;
}

void loop() {

   while (Serial.available() > 0 ) {

     incoming = Serial.readString().toInt();

     if (incoming == 0) {
        //Serial.println("identified_right");
        count = count-15;
        Serial.println(count);
        pwm.setPWM(0, 0, pulseWidth(count));
        delay(20);
        
     }
     
     else if (incoming == 1) {
        //Serial.println("identified_left");
        count = count+15;
        Serial.println(count);
        pwm.setPWM(0, 0, pulseWidth(count));
        delay(20);
        
     }
     
     else {
        //Serial.println("unknown");
     }

     if (count == 0 || count == 180){
      count = 90;
      pwm.setPWM(0, 0, pulseWidth(count));
      //delay(2000);
      }

      if (incoming == 2) {
        //Serial.println("identified_up");
        count1 = count1-15;
        Serial.println(count1);
        pwm.setPWM(1, 0, pulseWidth(count1));
        delay(20);
        
     }
     else if (incoming == 3) {
        //Serial.println("identified_down");
        count1 = count1+15;
        Serial.println(count1);
        pwm.setPWM(1, 0, pulseWidth(count1));
        delay(20);
        
     }

     if (count1 == 0 || count1 == 180){
      count1 = 90;
      pwm.setPWM(1, 0, pulseWidth(count1));
      //delay(2000);
      }
      if (incoming == 4) {
        //Serial.println("identified_down");
        
        pwm.setPWM(1, 0, pulseWidth(90));
        delay(20);
        pwm.setPWM(0, 0, pulseWidth(90));
         delay(20);
        
     }

   }
   

   }

/*void loop() {
 if (Serial.available() > 0) {
  incoming = Serial.readString();
  Serial.println(incoming);
  if (incoming.equals("move right")){
  count = count-50;
  
  Serial.print(count);
  pwm.setPWM(0, 0, pulseWidth(count));
delay(1000);
  }}
/*pwm.setPWM(0, 0, pulseWidth(0));
delay(1000);
pwm.setPWM(1, 0, pulseWidth(0));
delay(500);
/*pwm.setPWM(0, 0, pulseWidth(90));
delay(1000);
*/
