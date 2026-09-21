class Node:
    def __init__(self, course=0, neighbours=[]):
        self.course = course
        self.neighbours = neighbours

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        checked = set()
        def isCycle(node, visited):
            if node.course in checked:
                return False
            visited.add(node.course)
            for ne in node.neighbours:
                if ne.course in visited:
                    return True
                else:
                    if isCycle(ne, visited):
                        return True
            
            visited.remove(node.course)
            checked.add(node.course)
        schedule = {}
        for course, pre in prerequisites:
            if course in schedule:
                cur = schedule[course]
                if pre in schedule:
                    prereq = schedule[pre]
                else:
                    prereq = Node(pre, [])
                    schedule[pre] = prereq
                cur.neighbours.append(prereq)
            else:
                cur = Node(course, [])
                schedule[course] = cur
                if pre in schedule:
                    prereq = schedule[pre]
                else:
                    prereq = Node(pre, [])
                cur.neighbours.append(prereq)
                schedule[pre] = prereq
                
        for course, node in schedule.items():
            if node and isCycle(node, set()):
                    return False
        return True
