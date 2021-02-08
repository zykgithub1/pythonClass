#include "Shape.h"

Shape::Shape()
{
	color = "white";
	cout << "Shape无参构造函数." << endl;
}
Shape::Shape(string c)
{
	this->color = c;
	cout << "shape有参构造函数." << endl;
}
Shape::~Shape()
{
	cout << "shape析构函数." << endl;
}
string Shape::getColor()
{
	return this->color;
}
void Shape::setColor(string c)
{
	this->color = c;
}
double Shape::getArea()
{
	return 0;
}
void Shape::display()
{
	cout << "[Shape Object]color=" << getColor() <<"面积="<<getArea()<<endl;
}