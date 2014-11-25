#include <coordinator.h>
#include <Arduino.h>

Coordinator::Coordinator(int id)
{
	char instruction[MAX_MSG];
	char lastInstruction[MAX_MSG];
	Wire.begin();
	Serial.begin(9600);
	int roverID = id;
	int senID;
	int senNum;
}

char* Coordinator::Reading()
{

	//Create a buffer for the result, and construct a query for the SENSOR device
	char reading[MAX_MSG]; 
	sendInstruction(SENSOR);

	//Ping the SENSOR device for its results
	Wire.requestFrom(SENSOR, MAX_MSG);
	
	//Read in results from SENSOR device
	int i = 0;
	while(Wire.available())
	{
		reading[i] = Wire.read();
		i++;
	}
	reading[i] = '\0';

	
	return strdup(reading);
}

void Coordinator::sendInstruction(int deviceID)
{
	Wire.beginTransmission(deviceID);
	Wire.write(strdup(instruction));
	Wire.endTransmission();
}

int Coordinator::receiveInstruction()
{
	int i = 0;

	//Check if theres any data on the serial line
	if(Serial.available())
	{

		//Copy the current instruction into lastInstruction, then zero out instruction
		strncpy(lastInstruction, instruction, sizeof(instruction));
		clearInstruction();

		//Read the data into instruction
		while(Serial.available())
		{
			instruction[i] = Serial.read();
			i++;
		}
		instruction[i] = '\0';

		return true;
	}

	return false;
}

void sendData(String data)
{
	Serial.print(data);
}

void Coordinator::setInstruction(char* instr, int len)
{
	strncpy(instruction, instr, len);
}

char* Coordinator::getInstruction()
{
	return strdup(instruction);
}

void Coordinator::setRoverID(int id)
{
	roverID = id;
}

int Coordinator::getRoverID()
{
	return roverID;
}

void Coordinator::clearInstruction()
{
	//Zero out instruction
	int i;
	for(i = 0; i < MAX_MSG; i++)
		instruction[i] = 0;
}

int Coordinator::parseInstruction()
{
	// Read in the first 4 characters after Command: 
	
	char temp[4];
	int i;
	for(i = 9; i < 13; i++)
		temp[i-9] = instruction[i];
	
	temp[i] = '\0';
	
	// If temp contains READ this is a sensor instruction
	if(strcmp(temp, "READ") == 0)
	{
		return SENSOR;
	}
	// If temp contains WRIT this is a rover instruction
	else if(strcmp(temp, "WRIT") == 0)
	{
		return ROVER;
	}
	else
	{
		return 0;
	}
}