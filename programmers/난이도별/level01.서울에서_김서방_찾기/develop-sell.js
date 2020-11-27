function solution(seoul) {
    let index = seoul.findIndex((i) => i === "Kim")
    return "김서방은 " + index +"에 있다";
}

// 문제 풀이: 
// 처음에는 배열의 길이보다 작은 배열을 뽑기 때문에 
// index를 빼기 위해 기존의 filter라는 함수를 쓰려고 했다. 
// 그러다가 filter 함수는 요소(배열의 원소) 내용을 
// 바꿀 수 없다는 것을 알게 되었다. 

// 그래서 고민하다가 구글링을 통해 findIndex라는 함수를 알게 되어
// 사용해서 풀게 되었다.

// 배운점: 
// console.log(seoul.indexOf('Kim'))
// indexOf 라는 함수도 동일한 역할을 한다. 

// console.log(seoul.filter((i) => i ==="Kim"))
// filter는 이런 경우 사용 용도가 불분명하다.
// filter는 string의 가운데 값이 뭐인 경우만 뺄 때, 
// 혹은 int값이 뭐보다 크거나 작은 경우 , 뺄 때 사용한다
