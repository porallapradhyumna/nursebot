#include <Servo.h>  //servo library
Servo myservo;      // create servo object to control servo
#include <Wire.h>
 
 #include <MPU6050_light.h>
 int present;
 MPU6050 mpu(Wire);
 unsigned long timer = 0;
//Ultrasonic sensor variables
float fin;
float ang_diff;
//motor controller pins
#define ENA 6
#define ENB 7
#define IN1 2
#define IN2 3
#define IN3 4
#define IN4 5
#define carSpeed 255
#define carSpeed2 150
int rightDistance = 0, leftDistance = 0;
String cmd = "";
String pre_cmd = "";
void forward(){ 
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, 1);
  digitalWrite(IN2, 0);
  digitalWrite(IN3, 1);
  digitalWrite(IN4, 0);
  //Serial.println("Forward");
}

void back() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, 0);
  digitalWrite(IN2,1);
  digitalWrite(IN3, 0);
  digitalWrite(IN4, 1);
  //Serial.println("Back");
}
void right() {
  analogWrite(ENA, carSpeed2);
  analogWrite(ENB, 0);
  digitalWrite(IN1, 1);
  digitalWrite(IN2, 0);
  digitalWrite(IN3, 0);
  digitalWrite(IN4, 1); 
  //Serial.println("Left");
}
void left() {
  analogWrite(ENA, 0);
  analogWrite(ENB, carSpeed2);
  digitalWrite(IN1, 0);
  digitalWrite(IN2, 1);
  digitalWrite(IN3, 1);
  digitalWrite(IN4, 0);
  //Serial.println("Right");
}
void stop() {
  digitalWrite(ENA, LOW);
  digitalWrite(ENB, LOW);
  digitalWrite(IN1, 1);
  digitalWrite(IN2, 1);
  digitalWrite(IN3, 1);
  digitalWrite(IN4, 1);
  //Serial.println("Stop!");
}





void setup() { 
  //myservo.attach(8);
  //myservo.write(90);// attach servo on pin 3 to servo object
  Serial.begin(9600);     
  Wire.begin();
  mpu.begin();
  mpu.calcGyroOffsets();                          // This does the calibration
  present =  mpu.getAngleZ() ;
  
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  stop();
  mpu.update();
  float init = mpu.getAngleZ();
  
}

        
void loop() {
 mpu.update() ; 
 fin = mpu.getAngleZ();
 ang_diff = fin - init ;
 init = fin;
 //delay(10);
 
if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    cmd = data;
    pre_cmd = data;
    
  }
/*int right_dis = right_Distance_test();
int left_dis = left_Distance_test();
  if (right_dis <= 20 || left_dis <= 20) 
  {
  pre_cmd = cmd;
  cmd = "stop";
  }
  else{
    cmd = pre_cmd;
    }*/
  
  if (cmd == "forward"){
    
     forward();
    }
  else if (cmd == "stop"){
    stop();
    }
  else if (cmd == "left"){
    
    left();
    }
  else if (cmd == "right"){
    
    right();
    }
  else if (cmd == "back"){
    back();
    }
  else if (cmd == "gyro"){
    
    }

    //mpu.update();  
 //Serial.println(mpu.getAngleZ());
/*
  /*rightDistance = right_Distance_test();
  Serial.print("Right: ");
  Serial.println(rightDistance);
  
   leftDistance = left_Distance_test();
   Serial.print("Left: ");
  Serial.println(leftDistance);*/
  /*  myservo.write(60);  //setservo position to right side
    delay(200); 
    rightDistance = right_Distance_test();

    myservo.write(120);  //setservo position to left side
    delay(200); 
    leftDistance = left_Distance_test();


    if((rightDistance > 50)&&(leftDistance > 50)){
      stop();
    }else if((rightDistance >= 20) && (leftDistance >= 20)) {     
      forward();
    }else if((rightDistance <= 10) && (leftDistance <= 10)) {
        stop();
        delay(100);
    }else if(rightDistance - 3 > leftDistance) {
        left();
        delay(100);
    }else if(rightDistance + 3 < leftDistance) {
        right();
        delay(100);
    }else{
      stop();
    }*/
    
}
