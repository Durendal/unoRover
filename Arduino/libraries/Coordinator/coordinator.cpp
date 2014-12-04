#include <coordinator.h>
#include <Arduino.h>

Coordinator::Coordinator(int id)
{
	int instruction[MAX_MSG];
	instruction[0] = ENDMSG;
	int lastInstruction[MAX_MSG];
	lastInstruction[0] = ENDMSG;
	int roverID = id;
}

void Coordinator::setRoverID(int id)
{
	roverID = id;
}

void Coordinator::setInstruction(int instruc[], int instrucLen)
{
	setLastInstruction();
	int i;
	for(i = 0; i < instrucLen && i < MAX_MSG; i++)
		instruction[i] = instruc[i];
}
void Coordinator::getInstruction(int* instruc)
{
	int i = 0;
	do
	{
		instruc[i] = instruction[i];
		i++;
	}while(instruc[i] != ENDMSG && i < MAX_MSG)
}
void Coordinator::setLastInstruction()
{
	int i = 0;
	do
	{
		lastInstruction[i] = instruction[i];
		i++;
	}while(instruction[i] != ENDMSG && i < MAX_MSG);
}
int Coordinator::getRoverID()
{
	return roverID;
}

int Coordinator::parseInstruction()
{
	// Read in the first 4 characters after Command: 
	int instType;
	switch(instruction[0])
	{
		case FWD:
		case BAC:
		case STP:
		case LFT:
		case RGT:
			instType = ROVER;
			break;
		case READ:
		case NUMS:
		case TYPS:
			instType = SENSOR;
			break;
	}
	return instType;

}