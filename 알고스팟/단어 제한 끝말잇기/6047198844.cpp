/*
요구사항 : 단어들의 목록이 주어질 때, 단어들을 전부 사용하고 게임이 끝나는지 여부 확인. 단어를 전부 사용한다면 어떤 순서로 사용하는지
입력 : 테스트 케이스의 수 C (1<=C<=50), 게임에서 사용할 수 있는 단어의 수 n (1<=n<=100)
출력 : 게임이 끝나는 방법이 없는 경우 : IMPOSSIBLE / 방법이 있는 경우 : 사용할 단어들을 빈 칸 하나씩을 사이에 두고 순서대로 출력.
*/

#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int outadj[26];
int inadj[26];
int adj[26][26];
vector<string> wordAdj[26][26];

/*
그래프가 오일러 서킷이나 오일러 트레일일때 해당 경로로 단어를 생성함.
*/
void makeWords(vector<int> &EulerCircuit) {
	for (int i = 1; i < EulerCircuit.size(); i++) {
		if (i > 1) cout << " ";
		cout << wordAdj[EulerCircuit[i - 1]][EulerCircuit[i]].back();
		wordAdj[EulerCircuit[i - 1]][EulerCircuit[i]].pop_back();
	}
	return;
}


/*
그래프가 오일러 서킷인지 오일러 트레일인지 둘다 아닌지를 판단 하는 함수
*/
bool isEulerCheck() {
	int plus = 0; 
	int minus = 0;
	for (int i = 0; i < 26; i++) {
		int diff = outadj[i] - inadj[i];
		if (diff < -1 || diff > 1) return false;
		if (diff == -1) minus++;
		else if (diff == +1) plus++;
	}
	return (plus == 0 && minus == 0) || (plus == 1 && minus == 1);
}

/*
오일러 서킷
	무향 그래프 : 각 정점에 인접한 간선이 짝수개
	방향 그래프 : 각 정점에서의 들어가는 간선과 나가는 간선의 수가 같아야한다.
오일러 트레일 (a에서 시작하고 b에서 끝나는)
	a는 나가는 간선의 수가 들어오는 간선보다 하나 많다.
	b는 들어오는 간선의 수가 나가는 간선보다 하나 많다.
	다른 정점에서는 나가는 간선과 들어오는 간선의 수가 같다.

오일러 서킷과 오일러 트레일을 찾아서 반환하는 함수
*/
void makeEulerCircuit(vector<int> &EulerCircuit, int here) {
	for (int there = 0; there < 26; there++) {
		while (adj[here][there]) {
			adj[here][there]--;
			makeEulerCircuit(EulerCircuit,there);
		}
	}
	EulerCircuit.push_back(here);
}

vector <int> getEulerCircuit() {
	vector <int> EulerCircuit;
	//오일러 트레일인 경우
	for (int i = 0; i < 26; i++) {
		if (outadj[i] - inadj[i] == 1) {
			makeEulerCircuit(EulerCircuit,i);
			reverse(EulerCircuit.begin(), EulerCircuit.end());
			return EulerCircuit;
		}
	}
	
	//오일러 서킷인 경우
	for (int i = 0; i < 26; i++) {
		if (outadj[i] == inadj[i]&&outadj[i]>0) {
			makeEulerCircuit(EulerCircuit, i);
			reverse(EulerCircuit.begin(), EulerCircuit.end());
			return EulerCircuit;
		}
	}

	//아무것도 아닌경우 빈 서킷반환
	return EulerCircuit;
}


/*
그래프를 만드는 함수.
i로 시작해서 j로 끝나는 단어들의 목록

그래프의 인접 행렬 표현 i와 j 사이의 간선수
i로 시작하는 단어의 수 == > i에서 나가는 간선의 수
j로 끝나는 단어의 수 == > j로 들어가는 간선의 수
*/
void makeGraph(vector<string>& words) {
	for (int i = 0; i < 26; i++)
		for (int j = 0; j < 26; j++)
			wordAdj[i][j].clear();
	memset(outadj, 0, sizeof(outadj));
	memset(inadj, 0, sizeof(inadj));


	for (int i = 0; i < words.size(); i++) {
		string word = words[i];
		int first = word[0] - 'a';
		int last = word.back() - 'a';
		outadj[first]++;
		inadj[last]++;
		adj[first][last]++;
		wordAdj[first][last].push_back(word);
	}
	return;
}

void solution() {
	int N;
	cin >> N;
	vector<string> words(N);
	for (int i = 0; i < N; i++)
		cin >> words[i];
	makeGraph(words);
	if (!isEulerCheck()) {
		cout << "IMPOSSIBLE";
		return;
	}
	vector<int> EulerCircuit = getEulerCircuit();
	//모든 단어가 연결되어야함
	if (EulerCircuit.size() != words.size() + 1) {
		cout << "IMPOSSIBLE";
		return;
	}
	makeWords(EulerCircuit);
	return;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		solution();
		cout << "\n";
	}
}