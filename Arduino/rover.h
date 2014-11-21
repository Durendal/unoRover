#ifndef ROVER_H
#define ROVER_H
#include "XBee.h"
class Rover
{
	public:
		XBee xbee;
	void moveForward();
	void moveBackward();
	void turn(int, int);
	void stopRover();
	int roverSpeed(int);
};

#endif