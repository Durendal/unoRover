#include "Rover.h"
#include "Arduino.h"
#include <AFMotor.h>

Rover::Rover(int id, int speed)
{
	id = id;
	AF_DCMotor motor1(1, MOTOR12_64KHZ); // create motor #2, 64KHz pwm
	AF_DCMotor motor2(2, MOTOR12_64KHZ); // create motor #2, 64KHz pwm
	
	//If the value entered for speed is out of the acceptable range we set it to 200
	roverSpeed((speed < 0 || speed > 255) ? 200 : speed); 
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
	   delay(10);
   }
}

void Rover::stopRover()
{
   motor1.run(RELEASE);
   motor2.run(RELEASE); 
}

int Rover::roverSpeed(int newSpeed)
{
   if(newSpeed < 0 || newSpeed > 255)
	  return 0;
   motor1.setSpeed(newSpeed);
   motor2.setSpeed(newSpeed);
   return 1;
}
