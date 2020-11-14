#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    int p_size = people.size();
    sort(people.begin(), people.end(), greater<int>());
    int min_element = p_size - 1;
    for (int i = 0; i <= min_element; i++) {
            answer++;
            if(people[i]+people[min_element] <= limit) {
                min_element--;
        }
    }


    return answer;
}

int main() {
    cout << solution({ 100,100,100,100,100,100 }, 100);
}