#ifndef RECTANGLE_H
#define RECTANGLE_H
#include "Shape.h"

class Rectangle :public Shape
{
private:
	double width;
	double height;

public:
	Rectangle();
	Rectangle(string c, double width, double height);
	~Rectangle();
	void setWidth(double d);
	void setHeight(double h);
	double getWidth();
	double getHeight();
	void display();
	double getArea();

};



#endif // !RECTANGLE_H
