#ifndef CIRCLE_H
#define CIRCLE_H
#include "Shape.h"
class Circle :public Shape
{
private:
	double radius;
public:
	Circle();
	Circle(string c,double r);
	~Circle();
	void setRaduis(double r);
	double getRadius();
	double getArea();
	void display();
};

#endif // !CIRCLE_H
