def dijkstras(graph,start):
    d={}
    for i in graph:
        if i not in d:
            d[i]=float('inf')
    d[start]=0
    vis=[]
    q=[start]
    while(q):
        m=9999
        for i in q:
            if(d[i]<m):
                m=d[i]
                start=i
        for i in graph[start]:
            if(i[0] not in vis):
                q.append(i[0])
                if(d[i[0]]>i[1]+d[start]):
                    d[i[0]]=i[1]+d[start]
                vis.append(start)
        q.remove(start)
    print(d.values)
    return d
graph={5:[(3,1),(6,3),(1,2)],1:[(5,2),(2,1)],2:[(6,2),(1,1)],3:[(5,1),(6,3)],2:[(1,1),(6,2)],6:[(5,3),(3,3),(2,2)]}
print(dijkstras(graph,5))