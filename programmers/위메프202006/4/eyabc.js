function solution(text) {
  const bracketStack = [];
  const textStack = {};
  const openReg = /\(|\{|\[/;
  const closeReg = /\)|\}|\]/;
  text = text.replace(/ /g, "");

  for(let i = 0 ; i < text.length; i++) {
    if (openReg.test(text[i])) bracketStack.push(text[i]);
    else if (closeReg.test(text[i])) {
      textStack[bracketStack.length] += " ";
      bracketStack.pop();
    }
    else {
      if (textStack[bracketStack.length]) {
        textStack[bracketStack.length] += text[i]
      } else textStack[bracketStack.length] = text[i]
    }
  }
  return Object.values(textStack).reverse()
    .join(',').trim()
    .replace(/ /g, ",")
    .replace(/,,/g, ",")
}

console.log(solution("((아디다스) 무료 (나이키 (풋살화)) 배송) 강남점 (축구)(잔디)") === "풋살화,아디다스,나이키,무료배송,축구,잔디,강남점");
console.log(solution("[지이크]신원") === "지이크,신원");
console.log(solution("(냉장고 (양문냉장고 (2형 (삼성전자 {nt3058}))))" ))
console.log(solution("(냉장고 (양문냉장고 (2형 (삼성전자 {nt3058}))))" )  === "nt3058,삼성전자,2형,양문냉장고,냉장고")
