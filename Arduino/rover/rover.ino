#include <AFMotor.h>
#include <rover.h>
#include <coordinator.h>
#include <Wire.h>

Rover rover1(200);
int instruction[MAX_MSG];
int newSpeed;

void setup() 
{
	Wire.begin(ROVER);
    Wire.onReceive(receiveEvent);
    Wire.onRequest(requestEvent);
    rover1.stopRover();
    command = STP;
}

void loop() 
{
    drive();
    delay(10);
    
}  

void drive()
{

	switch(instruction[0])
	{
		case FWD:
			rover1.moveForward();
			break;
		case LFT:
			rover1.turn(0);
			break;
		case BAC:
			rover1.moveBackward();
			break;
		case RGT:
			rover1.turn(1);
			break;
        case SPD:
            rover1.roverSpeed(instruction[1]);
            break;
		case STP:
		default:
			rover1.stopRover();
			break; 				
        }        
}

void receiveEvent(int num)
{
    if(Wire.available())
    {
        int i = 0;
        do
        {
            instruction[i] = Wire.read();
            i++;
        }while(instruction[i] != ENDMSG && i < MAX_MSG);

    }
}

void requestEvent()
{
    Wire.write(rover1.getSpeed());
}