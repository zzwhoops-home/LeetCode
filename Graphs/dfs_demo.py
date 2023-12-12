from collections import deque

def depthFirstIterativePreOrder(graph, src):
    stack = deque([src])
    visited = set()

    while len(stack) > 0:
        cur = stack.pop()
        if cur not in visited:
            print(cur)
            visited.add(cur)

        for i in range(len(graph[cur]) - 1, -1, -1):
            stack.append(graph[cur][i])

def depthFirstIterativePostOrder(graph, src):
    stack = deque([src])
    visited = set()

    while len(stack) > 0:
        cur = stack.pop()
        if cur not in visited:
            print(cur)
            visited.add(cur)

        for vertex in graph[cur]:
            stack.append(vertex)

def depthFirstRecursive(graph, src):
    print(src)
    for vertex in graph[src]:
        depthFirstRecursive(graph, vertex)

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

if __name__==("__main__"):
    # depthFirstIterativePreOrder(graph, 'a')
    # depthFirstIterativePostOrder(graph, 'a')
    # print()
    depthFirstRecursive(graph, 'a')