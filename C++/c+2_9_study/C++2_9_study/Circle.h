#include "Shape.h"

class Circle :public Shape
{
private:
	double radius;
public:
	Circle();
	Circle(string c, double r);
	double getArea();
	void setRadius(double r);
	double getRadius();
};