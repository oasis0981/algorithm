def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [], # 문제에서 대부분 1번노드부터 시작하므로 0번은 비워둠
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트), 인덱스 0은 사용하지 않음
visited =[False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)