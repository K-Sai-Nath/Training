ip=[3,4]
cost=6
dp=[[-1 for i in range(len(ip)+1)] for j in range(cost+1)]
def dfs(ip,cost,idx):
    if cost==0:
        return 0
    if idx==len(ip):
        return float('inf')
    if dp[cost][idx]!=-1:
        return dp[cost][idx]
    if ip[idx]<=cost:
        take=1+dfs(ip,cost-ip[idx],idx)
        dp[cost][idx]=take
    else:
        take=float('inf')
        dp[cost][idx]=take
    nottake=dfs(ip,cost,idx+1)
    dp[cost][idx]=nottake
    dp[cost][idx]=min(take,nottake)
    return min(take,nottake)
print(dfs(ip,cost,0))