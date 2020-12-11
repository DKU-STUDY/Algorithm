#include <iostream>
#include <vector>
#include <math.h>

using namespace std;


int main()
{
	int N;
	vector <int> v(10000001);

	cin >> N;
	v[1] = 1;
	for (int i = 2; i <= 3162; i++)
	{
		if (!v[i])
			for (int j = i + i; j <= N; j += i)
				v[j] = 1;
	}

	int prime;
	do
	{
		for (int i = 2;i<=N; i++)
		{
			if (!v[i])
				if (!(N % i))
				{
					cout << i << "\n";
					prime = i;
					break;
				}
		}
	} while (N /= prime);
}
