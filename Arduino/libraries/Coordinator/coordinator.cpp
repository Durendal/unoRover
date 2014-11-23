#include <coordinator.h>
#include <Arduino.h>

Coordinator::Coordinator()
{
	XBee xbee = XBee();
	XBeeAddress64 hal9000 = XBeeAddress64(0x0013a200, 0x40bf058f);//Controller XBee address
	XBeeAddress64 davidBowman = XBeeAddress64(0x0013a200, 0x40c41907);//Coordinator XBee address
	uint8_t payload[MAX_FRAME_DATA_SIZE];
	ZBRxResponse Rx = ZBRxResponse();
	SoftwareSerial sserial(0,1);
	char* instruction;
	Wire.begin();
}

int Coordinator::Reading(int ownerNum, int deviceType, int deviceNum)
{
	char reading[1024];
	Wire.beginTransmission(ownerNum);
	Wire.write("COMMAND: READ " + ownerNum + ":" + deviceType + ":" + deviceNum);
	Wire.endTransmission();
	Wire.requestFrom(5, 1024);
	int i = 0;
	while(Wire.available())
	{
		reading[i] = Wire.read();
		i++;
	}
	reading[i] = '\0';

	return strdup(reading);
}

void Coordinator::setInstruction(char* instruction, int deviceNum)
{
	Wire.beginTransmission(deviceNum);
	Wire.write(strdup(instruction));
	Wire.endTransmission();
}

char* Coordinator::getInstruction()
{
	xbee.readPacket(100);

	char* instruction;
	if(xbee.getResponse().isAvailable())
	{
		if(xbee.getResponse().getApiId() == ZB_RX_RESPONSE)
		{
			xbee.getResponse().getZBRxResponse(Rx);
		}
	}
	else
		return false;
	
	return strdup(instruction);
}

void setRxXBeeAddress(int addr)
{
	davidBowman = XBeeAddress64(0x0013a200, addr);
}

void setTxXBeeAddress(int addr)
{
	hal9000 = XBeeAddress64(0x0013a200, addr);
}