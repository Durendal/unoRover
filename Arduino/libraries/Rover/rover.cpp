#include <rover.h>
#include <Arduino.h>

Rover::Rover(int id, int rspeed, int inst) : motor1(1, MOTOR12_64KHZ), motor2(2, MOTOR12_64KHZ)
{  
	int instruction = inst;
	int lastInstruction;
    int rid = id;
	roverSpeed(rspeed); 
	stopRover();
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

void Rover::turn(int dir, int ang)
{
   int counter = 0;
   while(counter < ang)
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
	   //delay(10);
   }
}

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

void Rover::setInstruction(int inst)
{
	lastInstruction = instruction;
	instruction = inst;
}

int Rover::getInstruction()
{
	return instruction;
}

void Rover::setLastInstruction(int inst)
{
	lastInstruction = inst;
}

void Rover::getLastInstruction()
{
	return lastInstruction;
}