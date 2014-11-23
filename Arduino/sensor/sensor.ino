#include <Wire.h>
#include <sensor.h>

Sensor sensor;
char instruction[1024];

void setup()
{
	 Wire.begin(2);
	 Wire.onRequest(requestEvent);
	 Wire.onReceive(receiveEvent);
	 int encoder1[] = {10};
	 int encoder2[] = {8};
	 int ultra1[] = {3, 11};
	 int ultra2[] = {9, 6};
	 sensor.addSensor(0, encoder1);
	 sensor.addSensor(0, encoder2);
	 sensor.addSensor(1, ultra1);
	 sensor.addSensor(1, ultra2);
}

void loop()
{
	 delay(10); 
}

void requestEvent()
{
	int command = 0;
	char* flags[] = {"COMMAND",
			 "READ",
			 "NUMSEN",
			 "TYPESEN"};
									
	int type, sensorNum;
	int i, j, k = 0;
	for(i = 0; i < 7; i++)
		if(instruction[i] != flags[0][i])
		{
			command = 1;
			break;
		}
	if(command == 0)
	{
		i += 2;
		for(j = 0; j < 4; j++)
			if(instruction[i+j] != flags[1][j])
			{
				command = 1;
				break;
			}
		if(command == 0)
		{
			i = i + j;
			i += 2;
			type = instruction[i];
			i += 2;
			sensorNum = instruction[i]; 
			if(type == 0)
				Wire.write(sensor.readSensor(sensorNum));
			else if(type == 1)
				Wire.write(sensor.readSensor((float)sensorNum));
		}
	}
	if(command == 1)
	{
		for(int j = 0; j < 6; j++)
			if(instruction[i + j] != flags[2][j])
			{
				command = 2;
				break; 
			}
		if(command == 1)
		{
			Wire.write(sensor.numSensors());
		}
	}
	if(command == 2)
	{
		for(int j = 0; j < 7; j++)
			if(instructions[i + j] != flags[3][j])
			{
				command = 3;
				break;
			} 
	
		if(command == 2)
		{
			i += 2;
			int sensorNum = (instruction[i] == '1' && instruction[i+1] == '0') ? 10 : instruction[i];
			Wire.write(sensor.sensorType(sensorNum)); 
		}
	}
	
}
void receiveEvent(int num)
{
	int i = 0;
	while(Wire.available())
	{
			instruction[i] = Wire.read();
			i++;
	}
	instruction[i] = '\0';
	
}
