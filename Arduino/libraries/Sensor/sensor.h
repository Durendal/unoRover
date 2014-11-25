#ifndef SENSOR_H
#define SONSOR_H
#include <Wire.h>
#include <Arduino.h>
#include <coordinator.h>

#define MAX_SENSORS 10
#define MAX_PINS 20

class Sensor
{
	public:
		Sensor();
		void addSensor(int type, int pin[]);
		int readSensor(int sensorNum, int type);
		int numSensors();
		int sensorType(int sensorNum);
	private:
		int sensors[10];
		int sensorCount;
		int pins[20];
};

#endif