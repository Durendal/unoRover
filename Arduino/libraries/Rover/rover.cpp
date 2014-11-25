#include <rover.h>

Rover::Rover(int rspeed) : motor1(1, MOTOR12_64KHZ), motor2(2, MOTOR12_64KHZ)
{  
	int command = 'h';
	char instruction[MAX_MSG];
	char lastInstruction[MAX_MSG];
	int turnAngle;
	roverSpeed(rspeed); 
	stopRover();
	Wire.begin(ROVER);
	 
}

void Rover::moveForward()
{
	motor1.run(FORWARD);
	motor2.run(BACKWARD);
}

void Rover::moveBackward()
{
   motor1.run(BACKWARD);
   motor2.run(FORWARD); 
}

void Rover::turn(int dir)
{
   int counter = 0;
   while(counter < turnAngle)
   {
	   //left turn
	   if(dir == 0)
	   {
		  motor1.run(BACKWARD);
		  motor2.run(BACKWARD);
	   } 
	   //right turn
	   else if(dir == 1)
	   {
		  motor1.run(FORWARD);
		  motor2.run(FORWARD); 
	   }
	   counter++;
   }
}

// HONK HONK!!
void Rover::stopRover()
{
   motor1.run(RELEASE);
   motor2.run(RELEASE); 
}

int Rover::roverSpeed(int newSpeed)
{

   //If the value entered for speed is out of the acceptable range we set it to 200
   newSpeed = (newSpeed < 0 || newSpeed > 255) ? 200 : newSpeed;
   motor1.setSpeed(newSpeed);
   motor2.setSpeed(newSpeed);
   return 1;
}

void Rover::setInstruction(char inst[])
{
	setLastInstruction();
	strncpy(instruction, inst, MAX_MSG);
}

char* Rover::getInstruction()
{
	return instruction;
}

void Rover::setLastInstruction()
{
	strncpy(lastInstruction, instruction, MAX_MSG);
}

char* Rover::getLastInstruction()
{
	return lastInstruction;
}

void Rover::setAngle(int angle)
{
	turnAngle = angle;
}

int Rover::getAngle()
{
	return turnAngle;
}

void Rover::setCommand(int com)
{
	command = com;
}

int Rover::getCommand()
{
	return command;
}