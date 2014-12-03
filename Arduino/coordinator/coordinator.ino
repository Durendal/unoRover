#include <Wire.h>
#include <coordinator.h>

//Coordinator coord(0);
int i2c;
String instruction;
char command;
char instruc_arr[MAX_MSG];
int sensorVal = 0;
int echoPin = 8;
int trigPin = 9;

void setup()
{
   Serial.begin(9600);
   instruction = "";
   Wire.begin();
   pinMode(echoPin, INPUT);
   pinMode(trigPin, OUTPUT);
   getReading();
}

void loop()
{
    if(receiveinstruction())
    {
        parseinstruction();
               
    }
    delay(100);
}
bool receiveinstruction()
{
        int c;
        instruction = "";
	//Check if theres any data on the serial line
	if(Serial.available())
	{
		while(Serial.available())
		{
			c = Serial.read();
			instruction += char(c);
                        delay(5);
		}
                //Serial.println("Received instruction: " + instruction);
		return true;
	}

	return false;
}

void parseinstruction()
{
        int i;
        int c;
        int data;
        instruction.toCharArray(instruc_arr, instruction.length());
	// If temp contains READ this is a sensor instruction
	if(instruction.indexOf("READ") != -1 || instruction.indexOf("NUMS") != -1 || instruction.indexOf("TYPE") != -1)
	{
             //getReading();

             Wire.beginTransmission(SENSOR);
             for(i = 0; i < instruction.length(); i++)
               Wire.write(instruc_arr[i]);
             Wire.endTransmission();
             Wire.requestFrom(SENSOR, 1);
             
             if(Wire.available())
             {
                sensorVal = Wire.read() << 8 | Wire.read();
             }
             Serial.print(sensorVal);
	}
	// If temp contains WRIT this is a rover instruction
	else if(instruction.indexOf("WRIT") != -1)
	{
                if(instruction.indexOf("FWD") != -1)
                   command = 'w';
                else if(instruction.indexOf("BAC") != -1)
                   command = 's';
                else if(instruction.indexOf("LFT") != -1)
                   command = 'a';
                else if(instruction.indexOf("RGT") != -1)
                   command = 'd';
                else if(instruction.indexOf("SPD") != -1)
                {
                  char rSpeed[4];
                  String roverSpeed = "p";
                  roverSpeed += instruction.substring(instruction.indexOf("SPD")+4);   
                  roverSpeed.toCharArray(rSpeed, 3);
                  Wire.beginTransmission(ROVER);
                  for(i = 0; i < 4; i++)
                    Wire.write(rSpeed[i]);
                  Wire.endTransmission();
                }
                else
                   command = 'h'; 
               Wire.beginTransmission(ROVER);
                 Wire.write(command);
               Wire.endTransmission();
		
	}

}

void getReading()
{
   long duration;

   digitalWrite(trigPin, LOW); 
   delayMicroseconds(5);
   
   digitalWrite(trigPin, HIGH);
   delayMicroseconds(10); 
   		 
   digitalWrite(trigPin, LOW);
   duration = pulseIn(echoPin, HIGH);
   sensorVal = ((duration/2)/29 > 255) ? 255 : (duration/2)/29;
   Serial.print(sensorVal);

}
