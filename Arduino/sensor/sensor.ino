#include <sensor.h>

Sensor sensor;
char instruction[1024];

void setup()
{
	 Wire.begin(SENSOR);
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
	char* flags[] = {
				"READ",
			 	"NUMS",
			 	"TYPE"
			};
									
	int type, sensorNum;
	int i, j, k = 0;
	char tmp[4];
	for(i = 0; i < 4; i++)
		tmp[i] = instruction[9+i];

	if(strncmp("COMMAND: ", instruction, 9))
	{
		if(strncmp(tmp, flags[0], 4))
		{
			type = instruction[15];
			sensorNum = instruction[17];

			if(type == 0)
				Wire.write(sensor.readSensor(sensorNum));
			else if(type == 1)
				Wire.write(sensor.readSensor((float)sensorNum));
		}
		else if(strncmp(tmp, flags[1], 4))
		{
			Wire.write(sensor.numSensors());
		}
		else if(strncmp(tmp, flags[2], 4))
		{
			int sensorNum = (instruction[15] == '1' && instruction[16] == '0') ? 10 : atoi(instruction[15]);
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
