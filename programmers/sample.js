function getPermutations(arr) {
    const result = [];

    function permute(current, remaining) {
        if (remaining.length === 0) {
            result.push(current.slice());
            return;
        }

        for (let i = 0; i < remaining.length; i++) {
            const next = current.concat(remaining[i]);
            const rest = remaining.slice(0, i).concat(remaining.slice(i + 1));
            permute(next, rest);
        }
    }

    permute([], arr);
    return result;
}

const inputArray = [1, 2, 3];
const permutations = getPermutations(inputArray);
console.log(permutations);
