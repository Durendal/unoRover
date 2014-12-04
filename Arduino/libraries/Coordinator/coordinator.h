#ifndef COORDINATOR_H
#define COORDINATOR_H

#include <Arduino.h>

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
#define MAX_MSG 64
#define COORDINATOR 0
#define ROVER 1
#define SENSOR 2
#define ENCODER 0
#define ULTRASONIC 1
#define CAMERA 2

/*
	Commands:
		These are the commands for the rover
*/		
#define ENDMSG 0x00
#define FWD 0x01
#define BAC 0x02
#define STP 0x03
#define LFT 0x04
#define RGT 0x05
#define GSP 0x06
#define SPD 0x07
#define READ 0x08
#define TYPS 0x09
#define NUMS 0x0A


class Coordinator
{
	public:

		Coordinator(int);
		void setRoverID(int);
		int getRoverID();
		void setInstruction(int[], int);
		void getInstruction(int*);
		void setLastInstruction();
		int parseInstruction();
		int instruction[MAX_MSG];
		int lastInstruction[MAX_MSG];
		int roverID;


};

#endif