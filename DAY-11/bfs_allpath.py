def bfs(graph,val):
    l.append(val)
    if val==2:
        print(l)
        l.pop()
        return
    for i in graph[val]:
        if i not in l:
            bfs(graph,i)
    l.pop()
graph = {5:[7,3],7:[5,4,3],3:[5,7,8],8:[2,4,3],4:[7,8,2],2:[4,8]}
l=[]
bfs(graph,5)
print(l)