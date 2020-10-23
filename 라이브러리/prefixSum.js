const getPrefixSum = (originArr) => {
  return originArr.reduce((prefixSum, num, key) => {
    prefixSum.push((num + prefixSum[key]));
    return prefixSum;
  }, [0]);
};