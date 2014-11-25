#ifndef COORDINATOR_H
#define COORDINATOR_H

#include <Arduino.h>
#include <Wire.h>

/*
	Constants:
		MAX_MSG - maximum size of message buffer
		COORDINATOR - Device ID for use in I2C communications
		ROVER - Device ID for use in I2C communications
		SENSOR - Device ID for use in I2C communications
		ENCODER - Sensor ID for encoders
		ULTRASONIC - Sensor ID for ultrasonic sensors
		CAMERA - Sensor ID for cameras
*/
#define MAX_MSG 1024
#define COORDINATOR 0
#define ROVER 1
#define SENSOR 2
#define ENCODER 0
#define ULTRASONIC 1
#define CAMERA 2

class Coordinator
{
	public:

		Coordinator(int id);
		int Reading();
		void sendInstruction(int deviceID);
		int receiveInstruction();
		void sendData(String data);
		void setInstruction(char* instr, int len = MAX_MSG);
		char* getInstruction();
		void setRoverID(int id);
		int getRoverID();
		int parseInstruction();
		int senID;
		int senNum;
	private:
		void clearInstruction();
		char instruction[MAX_MSG];
		char lastInstruction[MAX_MSG];
		int roverID;


};

#endif