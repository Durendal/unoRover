#include <Wire.h>
#include <coordinator.h>

//Coordinator coord(0);
int i2c;
int sensorResult;
int encoderPin = 12;
String instruction;
long counter = 0;
int nextmove = 0;
long encoderRead = 0;
long roundCount = 0;
void setup()
{
   Serial.begin(9600);

   pinMode(encoderPin, INPUT);
   instruction = "";
   Wire.begin();
}

void loop()
{
    
    char* moves[] = {
                      "COMMAND: WRIT MOVE FWD",
                      "COMMAND: WRIT MOVE BAC",
                      "COMMAND: WRIT TURN LFT",
                      "COMMAND: WRIT TURN RGT"
                    };    
    if(receiveInstruction())
    {
        i2c = parseInstruction();
        encoderRead = (instruction[0] == 'h') ? 0 : encoderRead;
        if(i2c == SENSOR)
        {
             //sensorResult = coord.Reading();
             //Wire.write(
             //coord.sendData("DATA: " + (String) coord.senID + ":" + (String) coord.senNum + " " + (String) sensorResult);
             1+1;
        }
        else if(i2c == ROVER)
        {
             int i = 0;
             Wire.beginTransmission(i2c);
             for(i = 0; i < instruction.length(); i++)
               Wire.write(instruction[i]);
             Wire.endTransmission();

             //coord.sendInstruction(ROVER);
        }
        
    }
    
    if(instruction[0] == 'a' || instruction[0] == 'd')
    {
        encoderRead += readEncoder(); 
        if(roundCount % 4299 == 0)
        {
             Serial.print("Encoder Ticks: ");
             Serial.println(encoderRead);
        }
    }
    roundCount++;
}
bool receiveInstruction()
{
        char c;
        instruction = "";
	//Check if theres any data on the serial line
	if(Serial.available())
	{
		while(Serial.available())
		{
			c = Serial.read();
			instruction += c;
		}
		return true;
	}

	return false;
}

int parseInstruction()
{
        return ROVER;
	
	// If temp contains READ this is a sensor instruction
	if(instruction.indexOf("READ") != -1)
	{
		return SENSOR;
	}
	// If temp contains WRIT this is a rover instruction
	if(instruction.indexOf("WRIT") != -1)
	{
		return ROVER;
	}
	else
	{
		return 0;
	}
}
int readEncoder()
{
   return digitalRead(encoderPin); 
}
