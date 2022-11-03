class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #here i is the start of the meetings thus we book a room and since 1 for +1. at the end of a meeting at j time we return the meeting room so -1. 
        # the conference rooms required is the max number of rooms we use at any point in the day which we keep track of in res. cur should in theory always 
        #be zero at the end of the code execution. 
        res = cur = 0
        print(sorted(x for i,j in intervals for x in [[i, 1], [j, -1]]))
        for i, v in sorted(x for i,j in intervals for x in [[i, 1], [j, -1]]):
            print("i", i)
            print("v", v)
            
            cur += v
            res = max(res, cur)
        return res
                