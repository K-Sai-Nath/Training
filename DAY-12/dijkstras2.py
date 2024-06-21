graph={0:[(1,2)],1:[(0,2),(3,3),(2,4)],2:[(1,4)],3:[(2,3)]}
def dijkstras(start,n):
    visited=set()
    queue=[(start,0)]
    distance=[float('inf')]*(n)
    distance[start]=0
    visited.add(start)
    while queue:
        node,cost=queue.pop(0)
        for i in graph[node]:
            if i[0] not in visited:
                distance[i[0]]=min(distance[i[0]],cost+i[1])
                queue.append((i[0],distance[i[0]]))
                visited.add(i[0])
    print(distance)
dijkstras(0,4)