#ifndef ROVER_H
#define ROVER_H
#include "XBee.h"
class Rover
{
	public:
		XBee xbee;
		int id;
	private:
		AF_DCMotor motor1();
		AF_DCMotor motor2();
	Rover(int id, int speed = 200);
	void moveForward();
	void moveBackward();
	void turn(int, int);
	void stopRover();
	int roverSpeed(int);
};

#endif