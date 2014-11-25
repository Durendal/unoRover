#include <Wire.h>
#include <coordinator.h>

Coordinator coord(0);
int i2c;
int sensorResult;
void setup()
{
   coord.setInstruction('w');
   coord.sendInstruction(ROVER);   
}

void loop()
{
    if(coord.receiveInstruction())
    {
        i2c = coord.parseInstruction();
        if(i2c == SENSOR)
        {
             sensorResult = coord.Reading();
             coord.sendData("DATA: " + (String) coord.senID + ":" + (String) coord.senNum + " " + (String) sensorResult);
        }
        else if(i2c == ROVER)
        {
             coord.sendInstruction(ROVER); 
        }
    }
}
