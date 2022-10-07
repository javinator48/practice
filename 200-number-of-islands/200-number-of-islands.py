class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def remove (i , j): 
            if (i < 0 or j < 0 or i==len(grid) or j== len(grid[0]) or grid[i][j]=="0"): 
                return
            grid[i][j]="0"
            remove(i,j+1) 
            remove(i,j-1)
            remove(i+1, j)
            remove(i-1, j)
        count = 0
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                 
                if grid[i][j] == "1": 
                    count += 1 
                    remove(i,j)
        return count
        
            
                
     
        