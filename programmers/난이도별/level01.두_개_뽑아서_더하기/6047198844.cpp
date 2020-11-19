#include <string>
#include <vector>
#include <set>
using namespace std;



vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    set<int> s;
    int numbers_size = numbers.size();
    for(int i=0;i<numbers_size-1;i++){
        for(int j=i+1;j<numbers_size;j++){
            s.insert(numbers[i]+numbers[j]);
        }
    }
    
    for(auto a : s){
        answer.push_back(a);
    }
    
    return answer;
}