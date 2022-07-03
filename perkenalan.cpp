#include<iostream>
using namespace std;

int arg()
{
    std::cout << "Nama Saya Ugel\nIni Hanyalah Perkenelan" ;
}

bool dead = false;
void goDeeper()
{
    if(dead == true)
        return;

    goDeeper();
}

int main(void)
{
    goDeeper();
}