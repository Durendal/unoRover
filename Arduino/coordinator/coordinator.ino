#include <Wire.h>
#include <coordinator.h>

Coordinator coord(0);
int i2c;
int sensorVal = 0;
int echoPin = 8;
int trigPin = 9;

void setup()
{
   Serial.begin(9600);

   Wire.begin();
   pinMode(echoPin, INPUT);
   pinMode(trigPin, OUTPUT);
   int nullCommand[] = { ENDMSG };
   coord.setInstruction(nullCommand, 1);
   getReading();
}

void loop()
{
    if(receiveinstruction())
    {
        int type;
        int msg[MAX_MSG];
        coord.getInstruction(msg);
        int i = 0;
        type = coord.parseinstruction();
        if(type == ROVER)
        {
           Wire.beginTransmission(ROVER);
           do
           {
              Wire.write(msg[i]);
              i++;
           }while(msg[i] != ENDMSG && i < MAX_MSG);
          Wire.endTransmission();
          if(msg[0] == GSP)
          {
             Wire.requestFrom(ROVER, 2);
             delay(10);
             sensorVal = Wire.read() << 8 | Wire.read();
             Serial.print(sensorVal); 
          }
        }
        else if(type == SENSOR)
        {
           Wire.beginTransmission(SENSOR);
           do
           {
              Wire.write(msg[i]);
              i++; 
           }while(msg[i] != ENDMSG && i < MAX_MSG);
           Wire.endTransmission();
           Wire.requestFrom(SENSOR, 2);
           delay(10);
           if(Wire.available())
           {
              sensorVal = Wire.read() << 8 | Wire.read();
           }           
           Serial.print(sensorVal);
        }
               
    }
    delay(100);
}
bool receiveinstruction()
{
        int c[MAX_MSG];
        int i = 0;
	//Check if theres any data on the serial line
	if(Serial.available())
	{
               do
               {
	            c[i] = Serial.read();
		    i++;
                    delay(5);
                }while(c[i] != ENDMSG);
                coord.setInstruction(c, i);
		return true;
	}

	return false;
}

