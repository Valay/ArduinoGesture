#include <Wire.h>
#include <L3G.h>
#include <LSM303.h>

L3G gyro;
LSM303 compass;

  float alpha = 0.8;
  
  float raw_acc_x = 0;
  float old_filtered_acc_x=0;
  float filtered_acc_x=0;

  float raw_acc_y = 0;
  float old_filtered_acc_y=0;
  float filtered_acc_y=0;

  float raw_acc_z = 0;
  float old_filtered_acc_z=0;
  float filtered_acc_z=0;

  float raw_gyro_x = 0;
  float old_filtered_gyro_x=0;
  float filtered_gyro_x=0;

  float raw_gyro_y = 0;
  float old_filtered_gyro_y=0;
  float filtered_gyro_y=0;

  float raw_gyro_z = 0;
  float old_filtered_gyro_z=0;
  float filtered_gyro_z=0;
  
  const int buttonPin = 2;     // the number of the pushbutton pin
  const int buttonPin2 = 8;     // the number of the pushbutton pin

void setup() {
  Serial.begin(9600);
  Wire.begin();

  if (!gyro.init())
  {
    Serial.println("Failed to autodetect gyro type!");
    while (1);
  }

  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);     
  pinMode(buttonPin2, INPUT);     
  
  gyro.enableDefault();
  
  compass.init();
  compass.enableDefault();
}

void loop() {
  gyro.read();

  /*Serial.print("G ");
  Serial.print("X: ");
  Serial.print((int)gyro.g.x);
  Serial.print(" Y: ");
  Serial.print((int)gyro.g.y);
  
  Serial.print(" Z: ");
  Serial.println((int)gyro.g.z);
  */
  compass.read();
  /*
  byte data[7];
  data[0] = (int)compass.a.x & 0x00FF;
  data[1] = (int)compass.a.x & 0xFF00;
  
  data[2] = (int)compass.a.y & 0x00FF;
  data[3] = (int)compass.a.y & 0xFF00;
  
  data[4] = (int)compass.a.z & 0x00FF;
  data[5] = (int)compass.a.z & 0xFF00;
  data[6] = ':';
  
  Serial.write(data, 7);
  */
  // Serial.print("A ");
  //Serial.print("X: ");
  


  
  raw_acc_x = compass.a.x;
  old_filtered_acc_x = filtered_acc_x;
  filtered_acc_x = alpha * old_filtered_acc_x + (1 - alpha) * raw_acc_x;

  raw_acc_y = compass.a.y;
  old_filtered_acc_y = filtered_acc_y;
  filtered_acc_y = alpha * old_filtered_acc_y + (1 - alpha) * raw_acc_y;

  raw_acc_z = compass.a.z;
  old_filtered_acc_z = filtered_acc_z;
  filtered_acc_z = alpha * old_filtered_acc_z + (1 - alpha) * raw_acc_z;
  

  raw_gyro_x = gyro.g.x;
  old_filtered_gyro_x = filtered_gyro_x;
  filtered_gyro_x = alpha * old_filtered_gyro_x + (1 - alpha) * raw_gyro_x;

  raw_gyro_y = gyro.g.y;
  old_filtered_gyro_y = filtered_gyro_y;
  filtered_gyro_y = alpha * old_filtered_gyro_y + (1 - alpha) * raw_gyro_y;

  raw_gyro_z = gyro.g.z;
  old_filtered_gyro_z = filtered_gyro_z;
  filtered_gyro_z = alpha * old_filtered_gyro_z + (1 - alpha) * raw_gyro_z;

  
  int diff_x = 100*(old_filtered_acc_x - filtered_acc_x);
  int diff_y = 100*(old_filtered_acc_y - filtered_acc_y);
  int diff_z = 100*(old_filtered_acc_z - filtered_acc_z);
  
  
  
  int buttonState = !(digitalRead(buttonPin));
  int buttonState2 = (digitalRead(buttonPin2));

  
  Serial.print(filtered_acc_x/1600.0);
  Serial.print(",");
  Serial.print(filtered_acc_y/1600.0);
  Serial.print(",");
  Serial.print(filtered_acc_z/1600.0);
  Serial.print(",");
  
  Serial.print((int)filtered_gyro_x);
  Serial.print(",");
  Serial.print((int)filtered_gyro_y);
  Serial.print(",");
  Serial.print((int)filtered_gyro_z);
  Serial.print(",");
  
  Serial.print((int)buttonState);
  Serial.print(",");
  Serial.println((int)buttonState2);
  
  
  
  /*
  compass.readMag();
  Serial.print("M ");
  Serial.print("X: ");
  Serial.print((int)compass.m.x);
  Serial.print(" Y: ");
  Serial.print((int)compass.m.y);
  Serial.print(" Z: ");
  Serial.println((int)compass.m.z);
*/
//delay(10);
}
