#include "Rectangle.h"


Rectangle::Rectangle()
{
	width = height = 1;
	cout << "Rectangle无参构造函数" << endl;
}
Rectangle::Rectangle(string c, double w, double h) :Shape(c)
{
    this->width = w;
	this->height = h;
	cout << "Rectangle的有参构造函数" << endl;
}
Rectangle::~Rectangle()
{
	cout << "Rectangle的析构函数" << endl;
}
void Rectangle::setWidth(double w)
{
	width = w;
}
void Rectangle::setHeight(double h)
{
	height = h;
}
double Rectangle::getWidth()
{
	return this->width;
}
double Rectangle::getHeight()
{
	return this->height;
}
double Rectangle::getArea()
{
	return width*height;
}
void Rectangle::display()
{
	cout << "[Rectangle Object]Color=" << getColor() << "面积为：" << getArea() << endl;
}