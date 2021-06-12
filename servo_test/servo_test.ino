#include "Wire.h"
#include "Adafruit_PWMServoDriver.h"
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40);

#define MIN_PULSE_WIDTH 600
#define MAX_PULSE_WIDTH 2600
#define FREQUENCY 50
int intial = 90;
int min_bound = 25;
int max_bound = 155;
String cmd = "";
  
void close_claw(){
  for(int i=140;i<=155;i++){
  //Serial.println(i);
  pwm.setPWM(4, 0, pulseWidth(i));
  delay(20);
  }
  }
void open_claw(){
  for(int i=155;i>=140;i--){
  //Serial.println(i);
  pwm.setPWM(4, 0, pulseWidth(i));
  delay(20);
  }
  }

  void relax(){
  pwm.setPWM(3, 0, pulseWidth(0));
  delay(500);
  pwm.setPWM(2, 0, pulseWidth(45));
  delay(500);
  pwm.setPWM(1, 0, pulseWidth(60));
  delay(500);
  close_claw();
  delay(500);
  pwm.setPWM(0, 0, pulseWidth(90));
  }

void active(){
  pwm.setPWM(0, 0, pulseWidth(90));
  delay(1000);
  pwm.setPWM(1, 0, pulseWidth(90));
  delay(1000);
  pwm.setPWM(2, 0, pulseWidth(90));
  delay(1000);
  pwm.setPWM(3, 0, pulseWidth(90));
  delay(1000);
  //pwm.setPWM(4, 0, pulseWidth(90));
  //delay(1000);
  close_claw();
  }
void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(FREQUENCY);
pwm.setPWM(0, 0, pulseWidth(90));
  delay(1000);
  pwm.setPWM(1, 0, pulseWidth(90));
  delay(1000);
  pwm.setPWM(2, 0, pulseWidth(90));
  delay(1000);
  pwm.setPWM(3, 0, pulseWidth(90));
  delay(1000);
  close_claw();
 /* pwm.setPWM(4, 0, pulseWidth(90));
  delay(1000);
  pwm.setPWM(5, 0, pulseWidth(90));
  delay(1000);
  pwm.setPWM(6, 0, pulseWidth(90));
  delay(1000);
  pwm.setPWM(7, 0, pulseWidth(90));
  delay(1000);*/
  //relax();
}
boolean l=true;
int pulseWidth(int angle) {
  int pulse_wide, analog_value;
  pulse_wide = map(angle, 0, 180, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
  analog_value = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
  return analog_value;
}

void loop() {
 /* for(int i=0;i<=180;i++){
     pwm.setPWM(0, 0, pulseWidth(i));
     pwm.setPWM(1, 0, pulseWidth(i));
     pwm.setPWM(2, 0, pulseWidth(i));
     pwm.setPWM(3, 0, pulseWidth(i));
      //pwm.setPWM(2, 0, pulseWidth(i));
      delay(100);}

       for(int i=180;i>=0;i--){
      pwm.setPWM(0, 0, pulseWidth(i));
     pwm.setPWM(1, 0, pulseWidth(i));
      pwm.setPWM(2, 0, pulseWidth(i));
      pwm.setPWM(3, 0, pulseWidth(i));
      delay(100);}*/
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.println(data);
    if (data == "active"){
      cmd = data;
      active();
      data = "10 12";
      }

    if (cmd == "active"){
    if (data == "open claw"){open_claw();
    data = "10 12";}
    if (data == "close claw"){close_claw();
    data = "10 12";}
    if (data == "relax"){relax();
      data = "10 12";}
    
    int str_len = data.length() + 1;
    char char_array[str_len];
    data.toCharArray(char_array, str_len);
    
    int servo_num = atoi(&char_array[0]);
    int angle = atoi(&char_array[2]);
    Serial.println(servo_num);
    Serial.println(angle);
    pwm.setPWM(servo_num, 0, pulseWidth(angle));
    //
  }
  }

  /*if(servo_num!="" && angle!=""){
    pwm.setPWM(servo_num, 0, pulseWidth(angle));
    }*/
}

  /*
 for(int i=0;i<=270;i++){
     pwm.setPWM(0, 0, pulseWidth(i));
     
      pwm.setPWM(1, 0, pulseWidth(i));
       pwm.setPWM(2, 0, pulseWidth(i));
        pwm.setPWM(3, 0, pulseWidth(i));
         pwm.setPWM(4, 0, pulseWidth(i));
    pwm.setPWM(5, 0, pulseWidth(i));
     pwm.setPWM(6, 0, pulseWidth(i));
  delay(200);
  }

   for(int i=270;i>=0;i--){
      pwm.setPWM(4, 0, pulseWidth(i));
     
      pwm.setPWM(1, 0, pulseWidth(i));
       pwm.setPWM(2, 0, pulseWidth(i));
        pwm.setPWM(3, 0, pulseWidth(i));
         pwm.setPWM(4, 0, pulseWidth(i));
    pwm.setPWM(5, 0, pulseWidth(i));
     pwm.setPWM(6, 0, pulseWidth(i));}
      delay(200);
      }
 /* if (l==true){

    for(int i=90;i>=0;i--){
      pwm.setPWM(0, 0, pulseWidth(i));
      delay(200);
      }
  for(int i=90;i<=120;i++){
    
    pwm.setPWM(1, 0, pulseWidth(i));
  delay(200);
  }

for(int i=0;i<=60;i++){
    
    pwm.setPWM(12, 0, pulseWidth(i));
  delay(200);
  }   

  for(int i=60;i>=0;i--){
    
    pwm.setPWM(12, 0, pulseWidth(i));
  delay(200);
  }   
  
  for(int i=0;i<=90;i++){
      pwm.setPWM(0, 0, pulseWidth(i));
      delay(200);
      }

   for(int i=120;i<=180;i++){
    
    pwm.setPWM(1, 0, pulseWidth(i));
  delay(200);
  }   

  for(int i=90;i<=180;i++){
    
    pwm.setPWM(3, 0, pulseWidth(i));
  delay(200);
  }   

  l=false;
  }
   /*for(int i=180;i>=intial;i-=1){
    pwm.setPWM(1, 0, pulseWidth(i));
   pwm.setPWM(2, 0, pulseWidth(i));
  delay(200);
  }
  
  /*pwm.setPWM(0, 0, pulseWidth(90));
pwm.setPWM(1, 0, pulseWidth(0));
pwm.setPWM(2, 0, pulseWidth(25));
  for(int i=180;i>=0;i-=1){
    pwm.setPWM(0, 0, pulseWidth(i));
    pwm.setPWM(1, 0, pulseWidth(i));
  delay(200);
  }
  /*pwm.setPWM(0, 0, pulseWidth(0));
  delay(500);
  pwm.setPWM(1, 0, pulseWidth(0));
  delay(500);
  pwm.setPWM(2, 0, pulseWidth(0));
  delay(500);
  pwm.setPWM(3, 0, pulseWidth(0));

  delay(1000);
  
  pwm.setPWM(0, 0, pulseWidth(180));
  delay(500);
  pwm.setPWM(1, 0, pulseWidth(180));
  delay(500);
  pwm.setPWM(2, 0, pulseWidth(180));
  delay(500);
  pwm.setPWM(3, 0, pulseWidth(180));
  
  
  /*delay(1000);
  pwm.setPWM(4, 0, pulseWidth(0));
  delay(1000);
  pwm.setPWM(0, 0, pulseWidth(180));
  pwm.setPWM(1, 0, pulseWidth(90));
  delay(500);
  pwm.setPWM(4, 0, pulseWidth(180));
  delay(1000);
  pwm.setPWM(0, 0, pulseWidth(90));
  pwm.setPWM(1, 0, pulseWidth(0));
  delay(1000);*/
//}
