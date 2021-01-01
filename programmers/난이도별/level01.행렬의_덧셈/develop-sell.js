function solution(arr1, arr2) {
  let out_len = arr1.length;
  let in_len = arr1[0].length;
  let array = [];
  for(let i = 0; i < out_len; i ++){
      let temp = []
      for(let j = 0; j < in_len; j++){
          temp.push(arr1[i][j] + arr2[i][j]);
      }
      array.push(temp)
  }
  return array;
}

// 문제풀이: 
// 빈 배열에 더한 값을 temp 변수에 넣고, temp를 
// 다시 배열에 push하는 방식으로 구현함. 

// 해결 안된 점: 
// 맨 처음에는 temp에 push하지 않고, array[i]에 바로 push하도록 했는데, 
// 값이 이상하게 들어가서 못 풀었습니다. 
// let array = Array(out_len).fill([]);
//   for(let i = 0; i < out_len; i ++){
//       for(let j = 0; j < in_len; j++){
//           array[i].push(arr1[i][j] + arr2[i][j]);
//       }
//   }

// 혹시 위 방식이 왜 안되는지 알 수 있을까요?? 

// 한줄 풀이: 
// return A.map((a,i) => a.map((b, j) => b + B[i][j]));

// 여기선 A부터 map으로 접근하고, 그 후에 또 다시 나온 값 a 배열의 map을
// 또 걸어서 그 값인 b에 B배열의 i,j 인덱스에 해당되는 값을 더한 배열을 return하도록 했다. 

