#include <stdio.h>
#define MAX 1001

int metrix[MAX][MAX];
int visited[MAX * MAX];

//깊이 우선 탐색
void DFS (int v, int N) {
	printf("%d ", v);
	visited[v] = 1;
  
	for (int d = 1; d <= N; d++) {
			if (!visited[d] && metrix[v][d]) {
			DFS(d, N);
		}
	}
}

//너비 우선 탐색
void BFS (int v, int N) {
	int front = -1, rear = -1;
	int queue[MAX * MAX] = { 0 };
	
	rear++;
	queue[rear] = v;
	
	visited[v] = 1;
	
	printf("%d ", v);

	while (front < rear) {
		front++;
		int nextV = queue[front];
	
		for (int d = 1; d <= N; d++) {
			if (!visited[d] && metrix[nextV][d]) {
				rear++;
				visited[d] = 1;
				queue[rear] = d;
				
				printf("%d ", d);
			}
		}
	}
}

void init (int N) {
	printf("\n");
	for (int i = 1; i <= N; i++) {
		visited[i] = 0;
	}
}

int main(void) {
	int N = 0;
	int M = 0;
	int V = 0;
	
	scanf("%d %d %d", &N, &M, &V);
	
	for (int i = 0; i < M; i++) {
		int s = 0;
		int d = 0;
		
		scanf("%d %d", &s, &d);
		
		metrix[s][d] = 1;
		metrix[d][s] = 1;
	}
	
	DFS(V, N);
	
	init(N);
	
	BFS(V, N);
	
	return 0;
}
