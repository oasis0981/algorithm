function solution(polynomial) {
    let terms = polynomial.split(" + ");

    let a = 0; // x 항
    let b = 0; // 상수항

    terms.forEach((el) => {
        if (el.includes("x")) {
            let temp = el.substring(0, el.indexOf("x"));
            if (temp == "") {
                a += 1;
            } else {
                a += Number(temp);
            }
        } else {
            b += Number(el);
        }
    });

    if (a === 0) {
        return `${b}`;
    }
    if (b === 0) {
        return `${a}x`;
    }
    if (a === 1) {
        return `x + ${b}`;
    }

    return `${a}x + ${b}`;
}
