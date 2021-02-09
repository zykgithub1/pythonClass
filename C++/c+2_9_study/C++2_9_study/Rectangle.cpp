#include "Rectangle.h"

Rectangle::Rectangle()
{
	width = 1;
	height = 1;
}
Rectangle::Rectangle(string c, double w, double h) :Shape(c), width(w), height(h)
{
	cout << "Rectangle的构造函数"<<endl;
}
void Rectangle::setWidth(double w)
{
	width = w;
}
void Rectangle::setHeight(double h)
{
	height=h;
}
double Rectangle::getWidth()
{
	return width;
}
double Rectangle::getHeight()
{
	return height;
}
double Rectangle::getArea()
{
	return height*width;
}