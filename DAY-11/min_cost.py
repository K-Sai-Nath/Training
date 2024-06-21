graph={5:[(7,12),(3,6)],7:[(5,12),(4,3),(3,2)],4:[(7,3),(8,2),(2,4)],8:[(3,4),(4,2),(2,3)],3:[(5,6),(7,2),(8,4)],2:[(4,4),(8,3)]}
res=[]
k=0
min_cost=float('inf')
min_path=[]
def dfs(start,visited,graph,end,out,k):
    global res,min_cost,min_path
    out.append(start)
    if start==end:
        res.append(out[:])
        if k<min_cost:
            min_cost=k
            min_path=out[:]
    for i in graph[start]:
        if i[0] not in out:
            dfs(i[0],visited,graph,end,out,k+i[1])
    out.pop()
dfs(5,set(),graph,2,[],0)
print(res)
print(min_cost)
print(min_path)
'''def bfs(start,graph,visited):
    queue=[start]
    out=[start]
    visited.add(start)
    while queue:
        node=queue.pop(0)
        for i in graph[node]:
            if i not in out:
                queue.append(i)
                out.append(i)
                visited.add(i)
    print(out)
bfs(5,graph,set())'''