function bfs(graph, start, visited) {
    visited[start] = true;
    let queue = [start];

    while (queue.length > 0) {
        let v = queue.shift();
        process.stdout.write(`${v} `);
        for (let i of graph[v]) {
            if (!visited[i]) {
                queue.push(i);
                visited[i] = true;
            }
        }
    }
}

const graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
];

const visited = Array.from({ length: 9 }, () => false);

bfs(graph, 1, visited);
