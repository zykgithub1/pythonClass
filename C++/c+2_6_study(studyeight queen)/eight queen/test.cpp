#include <iostream>
#include <stdio.h>
#include <stdbool.h>
using namespace std;

int number = 0;
bool flag[8] = { 1, 1, 1, 1, 1, 1, 1, 1, };
int place[8] = { 0 };
bool d1[15] = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
bool d2[15] = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
void print();
void Queen(int n);
int main()
{
	Queen(0);
	return 0;
}

void Queen(int n)
{
	int col;
	for (col = 0; col < 8; col++)
	{
		if (flag[col] && d1[n - col + 7] && d2[n + col])
		{
			place[n] = col;
			d1[n - col + 7] = 0;
			d2[n + col] = 0;
			flag[col] = 0;
			if (n < 7)
				Queen(n+1);
			else
			{
				print();
			}
			d1[n - col + 7] = 1;
			d2[n + col] = 1;
			flag[col] = 1;
		}
	}
}
void print()
{
	number++;
	int i, j;
	int area[8][8] = { 0 };
	printf("第一%d种情况：\n", number);
	for (i = 0; i < 8; i++)
	{
		area[i][place[i]] = 1;
	}
	for (i = 0; i < 8; i++)
	{
		for (j = 0; j < 8; j++)
		{
			printf("%d ", area[i][j]);
		}
		printf("\n");
	}
}