#include <string>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int n = sqrt(yellow);
    for(int y_height=1;y_height<=n;y_height++){
        if(!(yellow%y_height)){
            int y_width = yellow/y_height;
            if(brown==(y_height*2+y_width*2+1*4)){
                if(y_width<y_height)
                    swap(y_width,y_height);
                answer.push_back(y_width+2);
                answer.push_back(y_height+2);
                return answer;
            }  
        }
    }
    
    
}