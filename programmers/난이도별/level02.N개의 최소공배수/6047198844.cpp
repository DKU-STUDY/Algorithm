#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <math.h>

using namespace std;

bool prime[101];

// false면 소수
void Sieve() {
    memset(prime, false, sizeof(bool) * 101);
    prime[0] = prime[1] = true;
    for (int i = 2; i <= 100; i++) {
        if (!prime[i]) {
            for (int j = i+i; j <= 100; j += i)
                prime[j] = true;
        }
    }
}

int solution(vector<int> arr) {
    int answer = 1;
    Sieve();
    map <int, int> mp;
    for (int num : arr) {
        map <int, int> tmp_mp;
        for (int i = 1; num!=1; i++) {
            if (!prime[i]) {
                while (!(num % i)) {
                    tmp_mp[i]++;
                    num /= i;
                }
            }
        }
        for (auto m : tmp_mp) {
            mp[m.first] = mp[m.first] > m.second ? mp[m.first] : m.second;
        }
    }
    for (auto m : mp)
        answer *= pow(m.first, m.second);
    return answer;
}