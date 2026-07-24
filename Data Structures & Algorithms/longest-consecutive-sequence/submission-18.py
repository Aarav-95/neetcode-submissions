class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_map = defaultdict(int)
        for i in nums:
            nums_map[i] = 0
        
        mcount = 0
        new = set(nums)
        print(new)
        for i in new:
            print("eeeeee", i)
            if nums_map[i] == 0:
                temp = 1
                j = i
                while j+1 in nums_map:
                    if nums_map[j+1] != 0:
                        temp += nums_map[j+1]
                        break
                    else:
                        nums_map[j+1] = temp
                        temp += 1
                        j += 1
                nums_map[i] = temp
                mcount = temp if temp > mcount else mcount
        
        return mcount
            