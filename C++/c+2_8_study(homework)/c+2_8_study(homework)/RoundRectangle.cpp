#include "RoundRectangle.h"

RoundRectangle::RoundRectangle()
{
	roundRadius = 1;
	cout << "roundRectangle无参构造" << endl;
}
RoundRectangle::RoundRectangle(string c, double w, double h, double r) :Rectangle(c, w, h), roundRadius(r)
{

	cout << "roundRectangle有参构造函数" << endl;
}
RoundRectangle::~RoundRectangle()
{
	cout << "roundRectangle析构函数" << endl;
}
void RoundRectangle::setRoundRadius(double r)
{
	this->roundRadius = r;
}
void RoundRectangle::display()
{
	cout << "[roundRectangle Object]Color =" << getColor() << "面积=" << getArea() << endl;
}
double RoundRectangle::getArea()
{
	return getWidth()*getHeight() - 0.86*roundRadius*roundRadius;
}
