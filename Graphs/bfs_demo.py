from collections import deque
import random

def bfs(graph, src):
    queue = deque()
    visited = {src}
    queue.append(src)

    while len(queue) > 0:
        cur = queue.popleft()
        print(cur)
        
        for vertex in graph[cur]:
            if vertex not in visited:
                visited.add(vertex)
                queue.append(vertex)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# graph = {}

# chars = list("abcdefghijklmnopqrstuvwxyz")
# for i in range(26):
#     cur = []
#     for j in range(random.randint(1, 5)):
#         cur.append(random.choice(chars))

#     graph[chars[i]] = cur

if __name__==("__main__"):
    # print(graph)
    bfs(graph, 'a')