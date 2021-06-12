#include <Wire.h>
 
 #include <MPU6050_light.h>
 float present;
 int data;
 MPU6050 mpu(Wire);
 unsigned long timer = 0;
 String cmd = "";
 void setup() {
   Serial.begin(9600);                           // Ensure serial monitor set to this value also    
                         
   Wire.begin();
   mpu.begin();
   
   mpu.calcGyroOffsets();                          // This does the calibration
    present =  mpu.getAngleZ() ;      
 }
 void loop() {
   mpu.update();  
   
     int diff = present - mpu.getAngleZ();
    
     Serial.println(diff);
     if (diff == 74 || diff == -74)
     {present =  mpu.getAngleZ() ;
     delay(50);
     }                        
   
   if (Serial.available() > 0) {
     data = Serial.parseInt();
    //cmd = data;
    //Serial.println(data);
   
  }
  if (data == 0){
    diff = 0;
    present =  mpu.getAngleZ(); 
    data = 1;
    }
 }
