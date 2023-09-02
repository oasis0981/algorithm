const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const inputC = +input[0];
const inputTestCase = [];

console.log(input);

for (let i = 1; i <= inputC; ++i) {
    const arr = input[i].split(" ").map((item) => +item);
    let newArr = [];
    for (let j = 1; j < arr.length; j++) {
        newArr.push(arr[j]);
    }
    const testCase = {
        N: arr[0],
        arr: newArr,
    };
    inputTestCase.push(testCase);
}
