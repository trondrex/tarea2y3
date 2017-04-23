#include "Miclase.h"

Miclase *miclase;
void setup() 
{

//Serial.begin(9600);
miclase=newMiclase;

}

void loop() 
{

miclase->generador_funciones();

}
