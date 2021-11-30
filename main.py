from collections import defaultdict
import heapq


def minSpanningTree(graph, startingVertex):
    mst = defaultdict(set)
    visitedVertex = set([startingVertex])
    edges = [
        (cost, startingVertex, to)
        for to, cost in graph[startingVertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visitedVertex:
            visitedVertex.add(to)
            mst[frm].add(to)
            for toNext, cost in graph[to].items():
                if toNext not in visitedVertex:
                    heapq.heappush(edges, (cost, to, toNext))

    return mst


myGraph = {
    1: {2: 28, 6: 10, 2: 14},
    2: {1: 28, 3: 16, 7: 14},
    3: {2: 16, 4: 12},
    4: {3: 12, 7: 18, 5: 22},
    5: {4: 22, 7: 22, 6: 25},
    6: {1: 10, 5: 25},
    7: {2: 14, 5: 24, 4: 18},
}

print(dict(minSpanningTree(myGraph, 1)))
# result -> {1: {2, 6}, 2: {3, 7}, 3: {4}, 4: {5}}
