// BOJ
// 2389번 문제: 설탕 배달

var n = Number(require('fs').readFileSync('/dev/stdin')); // BOJ 제출용 코드. 입력값을 받는 코드이며 입력값을 숫자로 받기 위해 Number로 감쌈 // 초기 n은 봉지에 나눠담을 설탕 n킬로그램을 의미

let three = 0; // 3kg짜리 봉지 개수
let five = Math.floor(n / 5); // 5kg짜리 봉지 개수
n %= 5;

while(five >= 0){
    if(n % 3 == 0){ // 5kg 봉지에 담고 남은 나머지 설탕의 무게가 3kg 봉지에 딱 나눠떨어지게 담긴다면
        three = Math.floor(n / 3); // 3kg짜리 봉지 개수 갱신
        n %= 3; // n은 0일 것 // 봉지에 담아야할 설탕을 모두 담았음
        break;

    }
    five--; // 5kg 봉지에 담고 남은 나머지 설탕의 무게가 3kg 봉지에 딱 떨어지게 담길 수 없다면 five를 감소시킴(5kg 짜리 봉지수를 한 개 감소시키는 것)
    n += 5; // 5kg 봉지를 감소시켰으니 남은 설탕의 무게도 +5 해줌
}

if (n==0){ // 봉지에 모두 잘 담겼다면
    console.log(five + three); // 봉지개수 출력
}
else{ // 정확하게 N킬로그램을 만들 수 없다면
    console.log(-1); // -1 출력
}
