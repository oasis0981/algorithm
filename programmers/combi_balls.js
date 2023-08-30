function solution(balls, share) {
    var answer = binomialCoefficient(balls, share);
    return answer;
}

/**
 * 이항계수 - 동적계획법 & 메모이제이션
 * 이항계수의 점화식: C(n,k) = C(n−1,k−1) + C(n−1,k)
 * 동적계획법: 큰 문제를 작은문제로 나누어 해결함.
 * 중복되는 작은 부분 문제들은 한 번만 계산하고 결과를 저장함
 * 이미 한번 계산된 식이라면 memo에 저장되어 있으므로 중복이 없음(기존 재귀와 차이점)
 */

function binomialCoefficient(n, k, memo = {}) {
    const memoKey = `${n}-${k}`;

    if (memo[memoKey] !== undefined) {
        return memo[memoKey];
    }

    if (k === 0 || k === n) {
        return 1;
    }

    const result =
        binomialCoefficient(n - 1, k - 1, memo) +
        binomialCoefficient(n - 1, k, memo);
    memo[memoKey] = result;
    return result;
}

console.log(solution(3, 2)); // 예상 결과: 3
console.log(solution(5, 3)); // 예상 결과: 10
