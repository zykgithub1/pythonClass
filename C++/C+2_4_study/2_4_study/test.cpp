#include <iostream>
using namespace std;

double sumArea(double* radius, int n)
{
	int i = 0; double ret = 0;
	for (i = 0; i < n; i++)
	{
		ret += (3.14*radius[i]);
	}
	return ret;
}
int main()
{
	int n; int i = 0;
	cin >> n; double d;
	double *radius = new double[n];
	for (i = 0; i < n; i++)
	{
		cin >> d;
		radius[i] = d;	
	}
	double mj = sumArea(radius, n);
	cout << "Ãæ»ý=" << mj << endl;
	for (i = 0; i < n; i++)
	{
		cout << radius[i]   ;
	}
	delete radius;
	for (i = 0; i < n; i++)
	{
		cout << radius[i];
	}
	return 0;
}