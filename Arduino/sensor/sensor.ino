#include <sensor.h>
#include <coordinator.h>
#include <Wire.h>

Sensor sensor1;
int pins = {9, 8};
int reading = 0;
int instruction[MAX_MSG];
void setup()
{
	Serial.begin(9600);
	//Initialise I2C connection
	Wire.begin(SENSOR);
	Wire.onRequest(requestEvent);
	Wire.onReceive(receiveEvent);
	pinMode(echoPin, INPUT);
	pinMode(trigPin, OUTPUT);
        sensor1.addSensor(ULTRASONIC, pins);
	reading = sensor1.readSensor(0, ULTRASONIC);
}

// wheeeee round and round and round we go
void loop()
{
	reading = sensor1.readSensor(0, ULTRASONIC);
	delay(10); 
}

//Callback for I2C request
void requestEvent()
{
        if(instruction[0] == READ)
        {
                Wire.write(reading);
        }
	else if(instruction[0] == NUMS)
        {
                Wire.write(sensor1.sensorCount);
        }
        else if(instruction[0] == TYPS)
        {
                Wire.write(sensor1.sensorType(instruction[1]));
        }
}

//Callback for I2C receive
void receiveEvent(int num)
{
	//Read in the new instruction from Wire
	int i = 0;
	if(Wire.available())
	{
                do
                {
        		instruction[i] = Wire.read();
        		i++;
                }while(instruction[i] != ENDMSG && i < MAX_MSG);
	}
	
}
