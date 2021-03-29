#define _USE_MATH_DEFINES
#include <math.h>
#include <iostream>

using namespace std;

int main() {
	double R;
	scanf("%lf", &R);
	printf("%.6lf\n%.6lf", (R * R * M_PI), (R * R * 2));
}