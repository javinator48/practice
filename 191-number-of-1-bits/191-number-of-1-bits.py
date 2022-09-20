class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        n_list = str(bin(n))
        print(n_list)
        for char in n_list:
            
            if char == '1': 
                count += 1
        return count
            
        