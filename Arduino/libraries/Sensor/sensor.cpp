#include <sensor.h>
/*
	types:
		0 - encoder
		1 - ultrasonic sensor
*/
/*
	Sensor()
		Constructor, defines sensor and pins arrays. Our sensors have at most 2 pins so the
		pins array is twice the size of the sensors array, allowing for sensors to be added in
		any order. Access to pins is via the (sensor # * 2) or (sensor # * 2 + 1) depending on
		which you would like to access. MAX_SENSORS is defined as 10 and MAX_PINS as 20 in sensor.h
		feel free to adjust this to suit your needs, however if a sensor with 3 or more pins is used
		the pins array will need to be expanded accordingly. 
*/
Sensor::Sensor()
{
	int sensors[MAX_SENSORS];
	int pins[MAX_PINS];
	sensorCount = 0;
}
/*
	addSensor(int type, int pin[])
		adds a sensor to the sensor object. It's type is defined as an int: 0 for encoders and 1 for
		ultrasonic sensors(you can expand on this with other types of sensors). You must also send an array of
		pins that denote where the sensor is wired to the arduino. 
*/
void Sensor::addSensor(int type, int pin[])
{
	sensors[sensorCount] = type;

	if(type == 0)
	{
		pins[sensorCount*2] = pin[0];
		pinMode(pins[sensorCount*2], INPUT);

	}
	else if(type == 1)
	{
		pins[sensorCount*2] = pin[0];
		pins[sensorCount*2+1] = pin[1];
		pinMode(pins[sensorCount*2], INPUT);
		pinMode(pins[sensorCount*2+1], OUTPUT);
	}
	sensorCount++;
}
/*
	readSensor(int sensorNum, int type)
		reads from sensorNum and returns the output
*/
int Sensor::readSensor(int sensorNum, int type)
{
	if(type == 0)
	{
			return digitalRead(pins[sensorNum*2]);
	}
	else if(type == 1)
	{
		int sensorNum = (int) sensorNum;
		digitalWrite(pins[sensorNum*2], LOW); 
		delayMicroseconds(2); 

		digitalWrite(pins[sensorNum*2], HIGH);
		delayMicroseconds(10); 
		 
		digitalWrite(pins[sensorNum*2], LOW);
		long duration = pulseIn(pins[sensorNum*2+1], HIGH);
		 
		//Calculate the distance (in cm) based on the speed of sound.
		return (int) duration/58.2;
	}

}

/*
	numSensors()
		returns the total number of installed sensors
*/
int Sensor::numSensors()
{
	return sensorCount;
}
/*
	sensorType(int sensorNum)
		returns the type of sensor at a given index in the sensors array.
*/
int Sensor::sensorType(int sensorNum)
{
	return sensors[sensorNum];
}