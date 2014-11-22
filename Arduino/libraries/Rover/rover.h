#ifndef ROVER_H
#define ROVER_H
#include <AFMotor.h>
#include <XBee.h>
class Rover
{
	public:
		XBee xbee;
		int instruction;
		int lastInstruction;
		Rover(int id, int rspeed);
		void moveForward();
		void moveBackward();
		void turn(int, int);
		void stopRover();
		int roverSpeed(int);
		void setInstruction(int);
		int getInstruction();
		void setLastInstruction(int);
		int getLastInstruction();
		
	private:
		AF_DCMotor motor1;
		AF_DCMotor motor2;
		int rid;
};

#endif