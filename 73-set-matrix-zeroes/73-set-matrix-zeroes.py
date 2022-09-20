class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        rows = len(matrix)
        columns = len(matrix[0])
        R, C = set(),set()
        for i in range(rows): 
            for j in range(columns): 
                if matrix[i][j] == 0: 
                    R.add(i)
                    C.add(j)
        for i in range(rows): 
            for j in range(columns): 
                if i in R or j in C: 
                    matrix[i][j] = 0 
#         hashMap = {}
#         #print(matrix[0][0])
        
#         for index in range(len(matrix)): 
#             indices = []
#             for idx, value in enumerate(matrix[index]):
#                 if value == 0: 
#                     indices.append(idx)
#             hashMap[index] = indices
#             #print(hashMap[index])
#         #rows 
#         for hashMapIndex in hashMap:
            
#             if  hashMap[hashMapIndex]: 
#                 for zero_column_index in hashMap[hashMapIndex]: 
#                     for rowNumber in range(len(matrix)): 
#                         matrix[rowNumber][zero_column_index] = 0
                        
                
                
#                 #replace whole row with 0 
#                 #columns 
#                 for index,value in enumerate(matrix[hashMapIndex]): 
                   
                  
#                     matrix[hashMapIndex][index] = 0 
        
        
              
                    
        
                
            

                
            
                   
        
        