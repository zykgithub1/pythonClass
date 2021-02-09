#include "Rectangle.h"

class RoundRectangle :public Rectangle
{
private:
	double roundRdius;
public:
	RoundRectangle();
	RoundRectangle(string c, double w, double h, double r);
	void setRoundR(double r);
	double getRoundR();
	double getArea();

};