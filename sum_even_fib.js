function fiboEvenSum(n) {
    const fibArray = [0, 1];
    for (let i = 1; fibArray[i] < n; i++) {
        fibArray.push(fibArray[i] + fibArray[i - 1])
    }
    let filteredArr = fibArray.filter( (element) => (element <= n) && (element % 2 == 0));
    let fibSum = filteredArr.reduce((acc, val) => acc + val)
    return fibSum
  }
