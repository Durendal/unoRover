#include <AFMotor.h>
#include <XBee.h>
#include <rover.h>

Rover rover1(0, 200);
unsigned int count = 0;

void setup() 
{
    Serial.begin(9600);
    Serial.println("Initializing Rover..");
}
 
void loop() 
{
  //On every ten millionth iteration send the instruction over serial
  //*FOR DEBUGGING PURPOSES REMOVE IN FINAL BUILD*
  if(count % 10000000)
    Serial.println(rover1.instruction);
    
  //Just so the number doesnt get too high. Stoned numbers are shifty and not to be trusted.
  if(count > 10000000)
    count = 0;
  count++;
  
  rover1.setInstruction((Serial.available() > 0) ? Serial.read() : rover1.instruction);
  
  switch(rover1.instruction)
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
