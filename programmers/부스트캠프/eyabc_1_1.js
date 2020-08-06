function solution (name_list) {
  for (const name of name_list) {
    let cnt = 0;
    for(const target of name_list) {
      if (target.indexOf(name) !== -1) cnt++;
      if (cnt > 1) return true;
    }
  }
  return false;
}

console.log(
  solution(['가을', '우주', '너굴']) === false,
  solution(['봄', '여울', '봄봄']) === true,
  solution(['너굴', '너울', '여울', '서울'],
  ) ===
  false,
);