class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
        dum1, dum2 = nums1, nums2
        added2 = sorted(dum1 + dum2)
        # print(added2)
        if len(added2) % 2 == 0:
            x = float((added2[(len(added2)//2)-1] + added2[(len(added2)//2)]) / 2)
            return x
        else:
            return added2[(len(added2))//2]