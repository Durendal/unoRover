#include "Rover.h"

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
