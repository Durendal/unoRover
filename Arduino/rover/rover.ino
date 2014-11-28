#include <AFMotor.h>
#include <rover.h>
#include <coordinator.h>
#include <Wire.h>

Rover rover1(200);
String instruction;
char command;
void setup() 
{
        Serial.begin(9600);
	Wire.begin(ROVER);
        Wire.onReceive(receiveEvent);
        rover1.stopRover();
        command = 'h';
        instruction = "";
}

void loop() 
{
    drive();
    delay(100);
    
}  

void drive()
{

	switch(command)
	{
		case 'w':
                case 'W':
                
			rover1.moveForward();
			break;
                case 'A':
		case 'a':
			rover1.turn(0);
			break;
                case 'S':
		case 's':
			rover1.moveBackward();
			break;
                case 'D':
		case 'd':
			rover1.turn(1);
			break;
                case 'H':
		case 'h':
		default:
			rover1.stopRover();
			break; 				
        }        
        delay(3000);
}

void receiveEvent(int num)
{
    char c;
    while(Wire.available())
    {
        c = Wire.read();
        instruction += c;
    }
    parseInstruction();
}

void parseInstruction()
{
   if(instruction.indexOf("FWD") != -1)
      command = 'w';
   else if(instruction.indexOf("BAC") != -1)
      command = 's';
   else if(instruction.indexOf("LFT") != -1)
      command = 'a';
   else if(instruction.indexOf("RGT") != -1)
      command = 'd';
   else
      command = 'h'; 
}

