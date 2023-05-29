import numpy
class Solution:
    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numpyVersion = numpy.array(board)
        
        for i in range(9): 
            #check if the columns are valid
            if not self.checkValidHelper(numpyVersion[:, i]): 
                return False
            #check if rows are valid
            if not self.checkValidHelper(numpyVersion[i, :]): 
                return False 
        #check if sub-boxes are valid
        for i in [[0,1,2],[3,4,5], [6,7,8]]: 
            for j in [[0,1,2],[3,4,5], [6,7,8]]:
                subbox = numpyVersion[i,j[0]:j[2]+1]
                flatten_list = [j for sub in subbox for j in sub]
                if not self.checkValidHelper(flatten_list): 
                    return False 
        return True

    

    def checkValidHelper(self, aList): 
        #given a list of 9 elements representing a row, column, or a sub-box. Check if it is valid. 
        filteredList = list(filter(lambda a: a != ".", aList))
        if len(set(filteredList)) != len(filteredList): 
            return False 
        #check if all values are less than 9
        elif not (all(int(x)<=9 for x in filteredList)): 
            return False 
        #at this point we can confidently say that no repeat elements and all numbers satisfy the requirement 1-9. 
        else: 
            return True
            
            
            
        
        
        
        
    