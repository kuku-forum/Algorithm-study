def dfs(n, alst, blst):
    if n == N:
        print(alst)
        print(blst)
        print()
        return
        
    
    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst, blst+[n])
    
    
N = 4

dfs(0, [], [])