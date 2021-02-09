#include "RoundRectangle.h"

RoundRectangle::RoundRectangle()
{
	roundRdius = 1;
}
RoundRectangle::RoundRectangle(string c, double w, double h, double r) :Rectangle(c, w, h), roundRdius(r)
{
	cout << "roundRectangle¹¹Ôìº¯Êý" << endl;
}
void RoundRectangle::setRoundR(double r)
{
	roundRdius = r;
}
double RoundRectangle::getRoundR()
{
	return roundRdius;
}
double RoundRectangle::getArea()
{
	return this->getHeight()*this->getWidth() - 0.86*roundRdius*roundRdius;
}