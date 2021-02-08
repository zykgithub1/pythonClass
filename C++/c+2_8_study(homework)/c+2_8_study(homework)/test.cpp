#include <iostream>
#include "Shape.h"
#include "Rectangle.h"
#include "RoundRectangle.h"
#include "Circle.h"
int main()
{
	Shape shape1, shape2("red");
	shape1.display();
	shape2.display();
	cout << endl;


	Circle cir1, cir2("blue", 6);
	cir1.display();
	cir2.display();
	cout << endl;

	Rectangle rec1, rec2("green", 5, 4);
	rec1.display();
	rec2.display();
	cout << endl;

	RoundRectangle rd1, rd2("black", 5, 4, 0.5);
	rd1.display();
	rd2.display();

	cout << "end  end------------" << endl;
	return 0;
}