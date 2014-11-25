#include <AFMotor.h>
#include <rover.h>
#include <coordinator.h>
#include <Wire.h>


Rover rover1(200);

void setup() 
{
	Serial.begin(9600);
	Wire.begin(ROVER);
}
 
void loop() 
{
	delay(0.01);
}
void drive()
{
        
	switch(rover1.getCommand())
	{
		case 'w':
			rover1.moveForward();
			break;
		case 'a':
			rover1.turn(0);
			break;
		case 's':
			rover1.moveBackward();
			break;
		case 'd':
			rover1.turn(1);
			break;
		case 'h':
		default:
			rover1.stopRover();
			break; 				
        }
}

void parseInstruction()
{
	char tmp[3];
	tmp[0] = rover1.instruction[19];
	tmp[1] = rover1.instruction[20];
	tmp[2] = rover1.instruction[21];
        char* flags[] = {"BAC",
                   "FWD",
                   "STP",
                   "LFT",
                   "RGT"};
	//Check for Move [FWD | BAC | STP] commands	
	if(strncmp(rover1.instruction, "COMMAND: WRIT MOVE ", 19) == 0)
	{
                if(strncmp(tmp, flags[0], 3))
                    rover1.setCommand('s');
                else if(strncmp(tmp, flags[1], 3))
                    rover1.setCommand('w');
                else
                    rover1.setCommand('h');
		drive();
	}
	else if(strncmp(rover1.instruction, "COMMAND: WRIT TURN ", 19) == 0)
	{
		char ang[3];
		ang[0] = rover1.instruction[23];
		ang[1] = rover1.instruction[24];
		ang[2] = (rover1.instruction[23] == ' ') ? '\0' : rover1.instruction[23];		
		rover1.setAngle(atoi(ang));
                if(strncmp(tmp, flags[3], 3))
                    rover1.setCommand('a');
                else if(strncmp(tmp, flags[4], 3))
                    rover1.setCommand('d');
                else
                    rover1.setCommand('h');
		drive();
	} 
}

void receiveEvent(int num)
{
	int i = 0;
	char inst[MAX_MSG];
	while(Wire.available())
	{
		inst[i] = Wire.read();
		i++;
	}
	inst[i] = '\0';
	rover1.setInstruction(inst);
	parseInstruction();
}
