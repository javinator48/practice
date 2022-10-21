# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#         """
#         from collections import defaultdict
#         courseDict = defaultdict(list)

#         for relation in prerequisites:
#             nextCourse, prevCourse = relation[0], relation[1]
#             courseDict[prevCourse].append(nextCourse)

#         path = [False] * numCourses
#         for currCourse in range(numCourses):
#             if self.isCyclic(currCourse, courseDict, path):
#                 return False
#         return True


#     def isCyclic(self, currCourse, courseDict, path):
#         """
#         backtracking method to check that no cycle would be formed starting from currCourse
#         """
#         if path[currCourse]:
#             # come across a previously visited node, i.e. detect the cycle
#             return True

#         # before backtracking, mark the node in the path
#         path[currCourse] = True

#         # backtracking
#         ret = False
#         for child in courseDict[currCourse]:
#             ret = self.isCyclic(child, courseDict, path)
#             if ret: break

#         # after backtracking, remove the node from the path
#         path[currCourse] = False
#         return ret
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = defaultdict(int)   
        graph = defaultdict(set)
        q = deque()
        
        # init the courses with 0 deg
        for i in range(numCourses):
            degree[i] = 0
        
        # add 1 to degree of course that needs prereq
        # build edge from prerequisite to child course (directed graph)
        for pair in prerequisites:
            degree[pair[0]] += 1
            graph[pair[1]].add(pair[0])
        
        # start bfs queue with all classes that dont have a prerequisite
        for key, val in degree.items():
            if val == 0:
                q.append(key)
                
        stack = []
        
        while q:
            curr = q.popleft()
            stack.append(curr)
            for child in graph[curr]:
                degree[child] -= 1
                if degree[child] == 0:
                    q.append(child)
        
        return len(stack) == numCourses