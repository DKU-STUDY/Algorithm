function solution(n) {
    let answer = 0;
    var arr = [];
    var big = 0;
    let amount = n;
    while(1){
        if(n / Math.pow(3, big) < 3){
            break; 
        }
        big++;
    }
    for(let i = big; i > -1; i-- ){
        if(amount == 0){
            arr.push('0')
            continue;
        }
        if( amount /  (Math.pow(3, i)*2) >= 1){
            amount -= (Math.pow(3, i)*2);
            arr.push('2')   
        }
        else if(amount / Math.pow(3, i) >= 1){
            amount -= Math.pow(3, i);
            arr.push('1')
        }
        else{
            arr.push('0');
        }
    }
    arr.reverse();
    let size = arr.length - 1;
    arr.forEach(function (e){
        answer += (Math.pow(3, size) * e)
        size--;
    })
    return answer;
}

// 문제풀이:
// 먼저 무한루프를 돌면서 3의 n제곱으로 나뉘는 값이 1,2인 경우의 n값을 구한다
// 여기서 n값은 big이고, big부터 0까지 계속 값을 나눈다.
// 먼저 (3의 n제곱 * 2)으로 나뉘는지 보고 나눠지면 '2'를 arr에 푸시한다
// 그 다음 3의 n제곱으로 나눠지는지 보고 나눠지면 '1'를 arr에 푸시한다 
// 마지막으로는 '0'를 푸시한다

// 그 후 array를 reverse해주고 
// array의 사이즈 -1 만큼 돌면서 3의 n제곱을 하나씩 줄면서 answer에 값에 더해준다. 

// 헷갈린 점 / 어려운 점:
// 1. for문 감소문
// - for(let i = 10 ; i > 0; i--)  => 감소문의 가운데 조건은 부등호가 '>'로 바꿔야하는데, 계속 헤맸다.

// 2. 3진법은 0,1,2까지 있다는 점
// - 2까지 있다는 것을 뒤늦게 캐치해서 경우를 추가해줬다! (처음엔 0,1만 있는줄 알았다)

// 배운점:
// 1. arr는 reverse()라는 함수가 있다! str는 따로 없으니 참고
// 2. forEach문도 array의 한 함수로 취급!! 다음에 짤 때 참고
// 3. Math.pow(n, m) => n의 m제곱 !! 

// 참고풀이:
// (1)
// n = n.toString(3).split('').reverse().join('')
// return parseInt(n, 3)

// toString(n)으로 10진법 => n진법으로 변경
// split('')으로 str 한 문자씩 저장한 배열 리턴 
// join('')으로 배열을 str으로 붙여서 리턴 
// parseInt(n, 3) n진법 => 10진법으로 변경 

// (2)
// return parseInt([...n.toString(3)].reverse().join(""), 3);

// [...str] => split('')와 같은 기능 구현 