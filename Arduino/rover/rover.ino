#include <AFMotor.h>
#include <XBee.h>
#include <rover.h>

Rover rover1(0, 200);
int instruction;

void setup() 
{
    Serial.begin(9600);
    Serial.println("Initializing");
}
 
void loop() 
{

  instruction = (Serial.available() > 0) ? Serial.read() : instruction;
  //Serial.println((char)instruction);
  switch(instruction)
  {
     case 'w':
        rover1.moveForward();
        break;
     case 'a':
        rover1.turn(0, 25);
        break;
     case 's':
        rover1.moveBackward();
        break;
     case 'd':
        rover1.turn(1, 25);
        break;
     case 'h':
     default:
        rover1.stopRover();
        break; 
  }

}



