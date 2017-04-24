#include "Miclase.h"

Miclase::Miclase()
{
        
    Serial.begin(9600);
   // canal1='A0';
   // canal2='A1';
}

void Miclase::osciloscopio()    
{
    option = Serial.read();
    
    if (option == '6')
    
    {
    valor_sensor = analogRead(A0);
    }
    
    else if (option == '7')
    
    {  
    valor_sensor = analogRead(A1);
    }
    
    else
    {

    }

    
    float voltaje = valor_sensor * (5.0 / 1023.0);
    Serial.println(voltaje);
    delay(400);

}
