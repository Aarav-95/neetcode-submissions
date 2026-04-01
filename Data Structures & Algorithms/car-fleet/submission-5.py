class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car becomes fleet -> 
        # time of car in front >= time of car behind
        sorted_pos = position.copy()
        sorted_pos.sort()
        speeds = {}
        for i in range(len(position)):
            speeds[position[i]] = speed[i]
        length = len(sorted_pos)
        stack = [sorted_pos[length-1]]
        r = length - 2
        while r >= 0:
            print(stack)
            time_l = (target - stack[-1]) / speeds[stack[-1]]
            time_r = (target - sorted_pos[r]) / speeds[sorted_pos[r]]
            if time_r > time_l:   
                stack.append(sorted_pos[r])
            r -= 1
        
        return len(stack)
