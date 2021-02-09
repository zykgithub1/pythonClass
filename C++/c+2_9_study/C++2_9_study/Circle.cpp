#include "Circle.h"

Circle::Circle()
{
	radius = 1;
}
Circle::Circle(string c, double r) :Shape(c), radius(r)
{
	cout << "this is Circle's construct" << endl;
}
double Circle::getArea()
{
	return radius*radius*3.1415;
}
void Circle::setRadius(double r)
{
	radius = r;
}
double Circle::getRadius()
{
	return radius;
}