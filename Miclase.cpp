#include "Miclase.h"

Miclase::Miclase()
{
        
    Serial.begin(9600);
   // canal1='A0';
   // canal2='A1';
}

void Miclase::generador_funciones()    
{
    option = Serial.read();
    
    if (option == '1')
    
    {
    valor_sensor = analogRead(A0);
    }
    
    else
    
    {  
    valor_sensor = analogRead(A1);
    }
    
    
    float voltaje = valor_sensor * (5.0 / 1023.0);
    Serial.println(voltaje);
    delay(200);

}