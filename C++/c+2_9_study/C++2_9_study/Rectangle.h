#include "Shape.h"

class Rectangle:public Shape
{
private:
	double width, height;
public:
	Rectangle();
	Rectangle(string c, double w, double h);
	void setWidth(double w);
	void setHeight(double h);
	double getWidth();
	double getHeight();
	double getArea();
};