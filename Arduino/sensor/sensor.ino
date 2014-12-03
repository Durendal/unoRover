#include <sensor.h>
#include <coordinator.h>
#include <Wire.h>
#include <types.h>


String instruction;
int echoPin = 8;
int trigPin = 9;
int reading = 0;

void setup()
{
        Serial.begin(9600);
	//Initialise I2C connection
	 Wire.begin(SENSOR);
	 Wire.onRequest(requestEvent);
	 Wire.onReceive(receiveEvent);
         pinMode(echoPin, INPUT);
         pinMode(trigPin, OUTPUT);
         getReading();
}

// wheeeee round and round and round we go
void loop()
{
         getReading();
	 delay(10); 
}

//Callback for I2C request
void requestEvent()
{

        Wire.write(reading);
      
}

//Callback for I2C receive
void receiveEvent(int num)
{
        instruction = "";
	//Read in the new instruction from Wire
        int c;
	while(Wire.available())
	{
		c = Wire.read();
		instruction += char(c);
	}
	
}

void getReading()
{
   long duration;

   digitalWrite(trigPin, LOW); 
   delayMicroseconds(5);
   
   digitalWrite(trigPin, HIGH);
   delayMicroseconds(10); 
   		 
   digitalWrite(trigPin, LOW);
   duration = pulseIn(echoPin, HIGH);
   reading = ((duration/2)/29 > 255) ? 255 : (duration/2)/29;
   Serial.println((int)reading);

}
