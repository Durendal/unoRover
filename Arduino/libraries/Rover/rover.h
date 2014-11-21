#ifndef ROVER_H
#define ROVER_H
#include <AFMotor.h>
#include <XBee.h>
class Rover
{
	public:
		XBee xbee;
		int instruction;
		Rover(int id, int rspeed, int inst);
		void moveForward();
		void moveBackward();
		void turn(int, int);
		void stopRover();
		int roverSpeed(int);
		void setInstruction(int);
		void getInstruction();
	private:
		AF_DCMotor motor1;
		AF_DCMotor motor2;
		int rid;

	
};

#endif