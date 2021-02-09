#include "Shape.h"
#include "Rectangle.h"
#include "RoundRectangle.h"
#include "Circle.h"


int main()
{
	int i;
	Shape *ptrShape[8];
	
	ptrShape[0] = new Circle;
	ptrShape[1] = new Circle("h",4);
	
	ptrShape[2] = new Rectangle;
	ptrShape[3] = new Rectangle("y", 3, 4);
	for (i = 0; i < 4; i++)
	{
		ptrShape[i]->getArea();
	}
	for (i = 0; i < 4; i++)
	{
		delete ptrShape[i]
	}

}