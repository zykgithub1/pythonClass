#include "Shape.h"

Shape::Shape()
{
	this->color = "white";
}
void Shape::setColor(string c)
{
	this->color = c;
}
string Shape::getColor()
{
	return color;
}
Shape::Shape(string c)
{
	this->color = c;
}