class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        
        for char in s: 
            if queue:
                if char == ")" and queue[-1] == "(":
                    queue.pop()
                    char = ""

                if char == "]" and queue[-1] == "[": 
                    queue.pop()
                    char = ""
                if char == "}" and queue[-1] == "{": 
                    queue.pop()
                    char = ""
                else:
                    queue.extend(char)
            else: 
                queue.extend(char)
        if len(queue)>0: 
            return False 
        else: 
            return True
            