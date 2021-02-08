#include <string.h>
#include <iostream>
using namespace std;
class Shape
{
private:
	string color;
public:
	Shape()
	{
		this->color = "red";
	}
	Shape(string color)
	{
		this->color = color;
		printf("有参构造函数！！！！！图形的颜色是%s\n", color);
	}
	~Shape()
	{
		cout << "shape的析构函数" << endl;
	}
	void getArea()
	{
		cout << "我不知道啥图形啊" << endl;
	}
	void setColor(string color)
	{
		this->color = color;
	}
	string getColor()
	{
		return this->color;
	}

};
class Circle :public Shape
{
private:
	double rid;
public:
	Circle()
	{
		Shape();
		this->rid = 1.0;
	}
	Circle(string color, double rid)
	{
		Shape();
		this->rid = rid;
	}
	~Circle()
	{
		cout << "Circle的析构函数" << endl;
	}
	void setRid(double rid)
	{
		this->rid = rid;
	}
	double getRid()
	{
		return rid;
	}
	void getArea()
	{
		cout << "圆的面积=" << 3.14*rid << endl;
	}
};
class Rectangle :public Shape
{
public:
	Rectangle()
	{
		Shape();
		width = 1.0;
		height = 1.0;
	}
	Rectangle(string color, double width, double height)
	{
		this->setColor(color);
		this->height = height;
		this->width = width;
	}
	~Rectangle()
	{
		cout << "Rectangle的析构函数" << endl;
	}
	void getArea()
	{
		cout << "矩形的面积=：" << height*width << endl;
	}
	void setWidth(double width)
	{
		this->width = width;
	}
	void setHeight(double height)
	{
		this->height = height;
	}
	double getWidth()
	{
		return this->width;
	}
	double getHeight()
	{
		return this->height;
	}
private:
	double width;
	double height;
};
class RoundRectangle :public Rectangle
{
private:
	double rid;
public:
	RoundRectangle()
	{
		Rectangle();
		rid = 1.0;
	}
	RoundRectangle(string color, double width, double height, double rid)
	{
		this->setColor(color);
		this->setHeight(height);
		this->setWidth (width);
		this->rid = rid;
	}
	void getArea()
	{
		cout << "圆角矩形的面积为:" << this->getHeight()*getWidth() - 0.86*rid*rid << endl;
	}
	double getRid()
	{
		return rid;
	}
	void setRid(double rid)
	{
		this->rid = rid;
	}
};

int main()
{
	Shape shape1;
	shape1.getArea();
	Shape shape2("yellow");
	shape2.getArea();
	Rectangle rec1;
	rec1.getArea();
	Rectangle rec2("black",4.0,5.0);
	rec2.getArea();
	Circle cir1;
	cir1.getArea();
	Circle cir2("blue",2.5);
	cir2.getArea();
	RoundRectangle round1;
	round1.getArea();
	RoundRectangle round2("green",10,10,1);
	round2.getArea();
	return 0;
}