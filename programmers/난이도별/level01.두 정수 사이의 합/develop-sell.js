function solution(a, b) {
    var answer = 0;
    var max = 0;
    var min = 0;
    if (a >= b){
        max = a;
        min = b;
    }
    else{
        max = b;
        min = a;
    }
        
    for (var i = min; i <= max; i++){
        answer += i;
    }
    return answer;
}

// 정말 너무 길게 생각 없이 짠거 같다.. 
// 아마 max나 min이라는 함수가 있지 않을까? 한 줄 코드는 불가능한가? 

// var result = 0
//     //함수를 완성하세요


//     return (a+b)*(Math.abs(b-a)+1)/2;

// 역시 한 줄 코드가 있었다. 
//  양 끝의 숫자의 합 * 숫자 개수 / 2 = 덧셈 1~n의 값  (가우스의 법칙)