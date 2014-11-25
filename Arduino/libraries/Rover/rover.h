#ifndef ROVER_H
#define ROVER_H
#include <AFMotor.h>
#include <coordinator.h>
class Rover
{
	public:
		char instruction[MAX_MSG];
		char lastInstruction[MAX_MSG];
		Rover(int rspeed);
		void moveForward();
		void moveBackward();
		void turn(int);
		void stopRover();
		int roverSpeed(int);
		void setInstruction(char []);
		char* getInstruction();
		void setLastInstruction();
		char* getLastInstruction();
		void setAngle(int);
		int getAngle();
		void setCommand(int);
		int getCommand();

	private:
		AF_DCMotor motor1;
		AF_DCMotor motor2;
		int turnAngle;
		int command;
};	

#endif