function solution(n) {
    let sum=0;
    for(let i=1;i<=n;i++)
    {
        if(n%i==0) //나누어 떨어지면(약수이면)
            sum+=i //약수이므로 더해준다.
    }
    return sum;
}


function solution(n) {
    let sum=0;
    return [ ...Array(n).keys() ]
        .map(i => i + 1)
        .filter(i => n % i == 0)
        .reduce((sum, i) => sum + i);
}

/*
Array(n)은 n개의 배열을 생성
Array(n).keys()는 배열의 key값에 대한 iterator(반복을 위해 설계된, 특별한 인터페이스를 가진 객체)를 만든다.
[ ...Array(n).keys() ] : n개의 배열의 키값에 대한 배열을 만든다.

즉 [...Array(5).keys()] 는 [0,1,2,3,4]가 된다.
그리고 이러한 iterator와 관련된 for문으로 for of가 있다.
(for...of 명령문은 반복가능한 객체 (Array, Map, Set, String, TypedArray, arguments 객체 등을 포함)에 대해서 반복하고 각 개별 속성값에 대해 실행되는 문이 있는 사용자 정의 반복 후크를 호출하는 루프를 생성합니다.)

그러한 for of를 담당하는 것이 있는데 Map객체 입니다.
Map 객체는 요소의 삽입 순서대로 원소를 순회합니다. for...of 반복문은 각 순회에서 [key, value]로 이루어진 배열을 반환합니다.


결과적으로
[...Array(n).keys()]는 0부터 n까지의 배열을 생성

.map(i=>i+1)을 통해 그다음으로 return하는것은 1부터 n까지로 알 수 있고
.filter(i=>n%i==0)을 통해 n이라는 값으로
map에서 return 한 값들이 나누어지면 true이므로 .reduce로 가고
false이면 .reduce로 가지않는다.
마지막으로 .reduce에서는 나누어떨어지는 값들이 온 것을 첫번째인자인 누산기 sum에다가 더해주는것을 반복하고 전부 끝나면 return한다.
 */
