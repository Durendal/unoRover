#ifndef ROVER_H
#define ROVER_H
#include <AFMotor.h>
#include <XBee.h>
class Rover
{
	public:
		XBee xbee;
		AF_DCMotor motor1;
		AF_DCMotor motor2;
		int rid;
	
		//Rover(int id, int rspeed = 200);
		Rover(int id, int rspeed);
		void moveForward();
		void moveBackward();
		void turn(int, int);
		void stopRover();
		int roverSpeed(int);

	
};

#endif