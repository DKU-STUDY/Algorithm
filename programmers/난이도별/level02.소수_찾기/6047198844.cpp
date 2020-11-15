#include <string>
#include <vector>
#include <cstring>
#include <set>

using namespace std;
bool prime[9999999]; // false이면 소수
bool check[7];
set <int> s;

void sieve() {
    memset(prime, false, sizeof(bool) * 9999999);
    prime[0] = prime[1] = true;
    for (int i = 2; i < 3200; i++) {
        if (!prime[i])
            for (int j = i + i; j <= 9999999; j+=i)
                prime[j] = true;
    }
}

void brute_force(string numbers, string string_n, int n,int cnt) {
    if (cnt == n) {
        int check_prime = stoi(string_n);
        if (!prime[check_prime])
            s.insert(check_prime);
        return;
    }

    int number_size = numbers.size();
    for (int i = 0; i < number_size; i++) {
        if (!check[i]) {
            check[i] = true;
            brute_force(numbers, string_n + numbers[i], n,cnt+1);
            check[i] = false;
        }
    }
}

int solution(string numbers) {
    int answer = 0;
    sieve();
    int numbers_size = numbers.size();
    memset(check, false, sizeof(bool) * 7);
    for (int i = 1; i <= numbers_size; i++)
        brute_force(numbers, "", i,0);
    answer = s.size();

    return answer;
}