function solution(s) {
  let arr = s.split(" ");
  arr = arr.map((str)=> {
      str = str.split("")
      str = str.map((char, index) => {
          return index % 2 === 0 || index === 0 ? char.toUpperCase() : char.toLowerCase()
      })
      str = str.join('')
      return str;
  })
  return arr.join(' ');
}

// 변수 설명:
// arr : 단어별 Array
// str : 단어, string 값. (ex. try)
// char : 단어의 한 글자 (ex. try의 t)
// index : 단어마다 나타나는 index값 (단어마다 새로고침된다)

// 문제풀이: 
// 배열을 공백 기준으로 나누고, map함수를 통해 각각 단어별로 접근하게 한다. 
// 다시 split함수로 단어를 char별로 나누고, 이를 map함수를 통해
// index가 짝수(0 포함)면 대문자, 아니면 소문자로 변환해서 return한다.
// 그렇게 변환된 str를 다시 join하면 단어별 배열이 되고,
// 다시 join를 ' ' 빈칸 기준으로 하면 해당 string 값이 나온다 

// 어려웠던 점:
// 1.처음에 단어(공백을 기준)이 무슨 말인지 잘 이해가 안 갔다..! 

// 2.원래는 map함수 안에서는 forEach문으로 돌려서 받으려고 했는데, 
// 잘못된 판단이었다. 
// 이 문제에서 요구한 건 배열 안의 값을 변경한 배열을 가져오는 것인데, 
// 이때는 무조건 map함수를 쓴다. 
// forEach는 배열의 요소에 접근하는 용도로만 사용할 때 쓴다. 즉 배열의 요소를 바꿀 때는 아니다. 
// (접근해서 해당 값들을 다른 식에 적용해야할 때 사용)
// 잘 확인해둘 것! 

// 반드시 가져가야할 점: 
// map, join, split 함수를 사용할 때, 함수가 적용된 객체를 다시 받는 변수를 둬야한다. 
// (이것 때문에 시간 낭비를 많이 했다)
// ex. str.split("") 그냥 이렇게만 하면 배열로 쪼개지지만, str이 그렇게 변경되는 것이 아니다. 
// 즉 str = str.split("") 이런식으로 받아주는 객체가 필요하다. 
// 아님 바로 return 문에 쓰던가.. 
// 앞으로 console 찍을 때도 반드시 console.log(str) 이렇게 말고, console.log(str.split("")) 이걸로 보자
// 헷갈리지 말자! 

function solution(s) {
  let arr = s.split(" ");
  arr = arr.map((str)=> {
      
      let even = false;
      str = Array.from(str, char => {
          even = !even;
          return even ? char.toUpperCase() : char.toLowerCase();
      }).join('')
      return str;
      
  })
  return arr.join(' ');
}


// 위 식의 eyabc.js님의 코드를 보고 수정해본 코드이다. 