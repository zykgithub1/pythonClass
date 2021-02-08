#ifndef ROUND_H
#define ROUND_H
#include "Rectangle.h"
class RoundRectangle :public Rectangle
{
private:
	double roundRadius;

public:
	RoundRectangle();
	RoundRectangle(string c, double w, double h, double r);
	~RoundRectangle();
	void setRoundRadius(double r);
	double getRoundRadius();
	double getArea();
	void display();
};


#endif // !ROUND_H
