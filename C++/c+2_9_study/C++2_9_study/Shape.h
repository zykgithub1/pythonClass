#ifndef SHAPE_H
#define SHAPE_H
#include <iostream>
#include <string>
using namespace std;

class Shape
{
private:
	string color;
public:
	Shape();
	Shape(string c);
	virtual double getArea() = 0;
	void setColor(string c);
	string getColor();
};

#endif // !1
