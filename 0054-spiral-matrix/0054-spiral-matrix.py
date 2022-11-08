class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #append first row 
        #remove first row 
        #reverse each row
        #Transpose matrix
        #Repeat steps 1-4 until matrix is empty
        answer = []
        while matrix: 
            answer.extend(matrix[0])
            matrix = matrix[1:]
            
            matrix = [amatrix[::-1] for amatrix in matrix]  
            #transpose matrix 
            if(len(matrix) <=0):
                break
                
            matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
            
        return answer
           
            
            
            
        
        