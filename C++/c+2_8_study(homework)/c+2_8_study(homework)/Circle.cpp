#include "Circle.h"
Circle::Circle()
{
	radius = 1;
	cout << "Circle无参构造函数." << endl;
}
//!!!!!!!!!!!!!!!!!!!!1
Circle::Circle(string c, double r) : radius(r), Shape(c)
{
	this->setColor(c);
	cout << "Circle有参构造函数" << endl;
}
Circle::~Circle()
{
	cout << "Circle析构函数" << endl;
}
void Circle::setRaduis(double r)
{
	radius = r;
}
double Circle::getRadius()
{
	return radius;
}
double Circle::getArea()
{
	return 3.14*radius*radius;
}
void Circle::display()
{
	cout << "[Circle Object] Color=" << getColor() << "Cirlce面积=" << getArea() << endl;
}