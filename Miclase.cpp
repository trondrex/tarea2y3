#include "Miclase.h"

Miclase::Miclase()
{
        
    Serial.begin(9600);
}

void Miclase::osciloscopio()    
{
    option = Serial.read();
    
    if (option == 'a')
    
    {
    valor_sensor = analogRead(A0);
    float voltaje = valor_sensor * (5.0 / 1023.0);
    Serial.println(voltaje);
    }
    
    else if (option == 'b')
    
    {  
    valor_sensor = analogRead(A1);
    float voltaje = valor_sensor * (5.0 / 1023.0);
    Serial.println(voltaje);
    }
    
    else
    {
    number = Serial.readStringUntil('z');     
    volta=number.toFloat();
    volta= volta * (225.0/5.0);    
    analogWrite(8,volta);
    Serial.println(volta);
    }

    
    delay(400);

}
