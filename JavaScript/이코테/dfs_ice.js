function dfs(x, y) {
    if (x <= -1 || x >= n || y <= -1 || y >= m) {
        return false;
    }

    if (graph[x][y] === 0) {
        graph[x][y] = 1;

        dfs(x - 1, y);
        dfs(x, y - 1);
        dfs(x + 1, y);
        dfs(x - 1, y);

        return true;
    }

    return false;
}

let result = 0;
for (let i; i < graph.length; i++) {
    for (let j; j < graph.length; j++) {
        if (dfs(i, j) === true) {
            result += 1;
        }
    }
}
