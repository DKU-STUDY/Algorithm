function solution(phone_number) {
  let len = phone_number.length;
  return phone_number.split('')
                      .map((value, index) => (len - index <= 4 ? value : "*"))
                      .join('');
}

// 문제풀이: 
// phone_number str를 한 글자씩 split하고, 
// 같은 사이즈의 배열의 조건에 따라 요소 값만 변하니까 map함수를 사용했다. 

// 그래서 배열의 전체 사이즈에서 인덱스("index")를 뺀 값이 4 이하인 경우만 
// 실제 값("value")를, 아니면 "*"를 반환하도록 했다. 

// 마지막으로 join('')으로 배열을 다시 str로 만들어준다. 

// 프로그래머스 풀이: 

// //1 정규식
// return s.replace(/\d(?=\d{4})/g, "*");

// 참고: https://beomy.tistory.com/21 

// //2 repeat
// var result = "*".repeat(s.length - 4) + s.slice(-4);

// 맨 뒤 4자리 빼고 앞 부분 : (s.length - 4)
// 만큼은 repeat 함수를 통해 "*"를 반복해서 str를 만들어준다. 

// 그 다음 뒤에 slice 함수를 통해, 맨 뒤 4자리를 짤라서 붙인다. 

// slice는 '음수'가 지원되니 slice를 쓰는 것을 추천한다 (즉, 뒤에서부터 index하는 것도 가능) <=> substr