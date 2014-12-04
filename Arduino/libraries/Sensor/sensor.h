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
		void addSensor(int, int []);
		int readSensor(int, int);
		int numSensors();
		int sensorType(int);
	private:
		int sensors[10];
		int sensorCount;
		int pins[20];
};

#endif