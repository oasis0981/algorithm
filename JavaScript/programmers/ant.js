function solution(hp) {
    let cnt = 0;
    const powers = [5, 3, 1];
    for (let power of powers) {
        if (hp / power > 0) {
            cnt += Math.floor(hp / power);
            hp %= power;
        }
    }

    return cnt;
}

console.log(solution(999));
