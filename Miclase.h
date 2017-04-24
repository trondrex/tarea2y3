#ifndef Miclase_h
#define Miclase_h
#include <Arduino.h>

class Miclase
{

public: 
    Miclase(); 
    void osciloscopio();
private:
    //char canal1;
    //char canal2;
    char option;
    float valor_sensor;
    float voltaje;
};


#endif
