#include <iostream>
#include <vector>
#include <climits>
#define INF INT_MAX

using namespace std;

void floyd(vector <vector<int>>&vt,int n) {
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if (i!=j && vt[i][k] != INF && vt[k][j] != INF)
					vt[i][j] = 1;
}

int main() {
	int n, k;
	scanf("%d %d", &n, &k);
	vector <vector<int>> vt(n + 1, vector<int>(n + 1,INF));
	int i, j;
	while (k--) {
		scanf("%d %d", &i, &j);
		vt[i][j] = 1;
	}
	floyd(vt, n);
	
	cin >> n;
	while (n--) {
		scanf("%d %d", &i, &j);
		if (vt[i][j] == 1)
			printf("-1\n");
		else if (vt[j][i] == 1)
			printf("1\n");
		else
			printf("0\n");
	}
}