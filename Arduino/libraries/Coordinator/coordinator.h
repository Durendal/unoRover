#ifndef COORDINATOR_H
#define COORDINATOR_H
#include <XBee.h>
#include <String.h>
#include <Arduino.h>
#include <queue.h>
#include <SoftwareSerial.h>
#include <Wire.h>

class Coordinator()
{
	public:
		XBee xbee;
		
		SoftwareSerial sserial(0,1);

		int getSensorReading(int sensorType, int sensorNum);
		void setInstruction(char* instruction);
		char* getInstruction();
		void setRxXBeeAddress(int addr);
		void setTxXBeeAddress(int addr);
	private:
		char* instruction;
		XBeeAddress64 hal9000;
		XBeeAddress64 davidBowman;

};

#endif