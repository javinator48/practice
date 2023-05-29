############################ SOLUTION 1 ############################
# import numpy
# class Solution:
    
    
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         numpyVersion = numpy.array(board)
        
#         for i in range(9): 
#             #check if the columns are valid
#             if not self.checkValidHelper(numpyVersion[:, i]): 
#                 return False
#             #check if rows are valid
#             if not self.checkValidHelper(numpyVersion[i, :]): 
#                 return False 
#         #check if sub-boxes are valid
#         for i in [[0,1,2],[3,4,5], [6,7,8]]: 
#             for j in [[0,1,2],[3,4,5], [6,7,8]]:
#                 subbox = numpyVersion[i,j[0]:j[2]+1]
#                 flatten_list = [j for sub in subbox for j in sub]
#                 if not self.checkValidHelper(flatten_list): 
#                     return False 
#         return True

    

#     def checkValidHelper(self, aList): 
#         #given a list of 9 elements representing a row, column, or a sub-box. Check if it is valid. 
#         filteredList = list(filter(lambda a: a != ".", aList))
#         if len(set(filteredList)) != len(filteredList): 
#             return False 
#         #check if all values are less than 9
#         elif not (all(int(x)<=9 for x in filteredList)): 
#             return False 
#         #at this point we can confidently say that no repeat elements and all numbers satisfy the requirement 1-9. 
#         else: 
#             return True

############################ SOLUTION 1.5 ############################

class Solution: 
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        # cols = {}
        # rows = {}
        # squares = {} 
        cols = collections.defaultdict(set) 
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = (r /3, c/3)
        for r in range(9): 
            for c in range(9): 
                if board[r][c] == ".": 
                    continue
                if not self.checkValidHelper(board, rows, cols, squares, r, c): 
                    return False 
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

    def checkValidHelper(self,aboard, arows, acols, asquares,  R,C):
        if ((aboard[R][C] in arows[R]) or (aboard[R][C] in acols[C]) or (aboard[R][C] in asquares[(R // 3, C //3)])): 
            return False 
        else: 
            return True
        
                
                

############################ SOLUTION 2 ############################

# class Solution: 
#     def isValidSudoku(self, board: List[List[str]]) -> bool: 
#         cols = collections.defaultdict(set) 
#         rows = collections.defaultdict(set)
#         squares = collections.defaultdict(set) #key = (r /3, c/3)
        
#         for r in range(9): 
#             for c in range(9): 
#                 if board[r][c] == ".": 
#                     continue
#                 if (board[r][c] in rows[r]
#                     or board[r][c] in cols[c]
#                     or board[r][c] in squares[(r // 3, c//3)]
                   
#                 ):
#                     return False 
#                 cols[c].add(board[r][c])
#                 rows[r].add(board[r][c])
#                 squares[(r // 3, c // 3)].add(board[r][c])
#         return True
        
        
        
        
    