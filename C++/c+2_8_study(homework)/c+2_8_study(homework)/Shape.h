#ifndef SHAPE_H
#define SHAPE_H
#include <string>
#include <iostream>
using namespace std;

class Shape
{
private:
	string color;
public:
	Shape();
	Shape(string c);
	~Shape();
	string getColor();
	void setColor(string c);
	double getArea();
	void display();
};
#endif