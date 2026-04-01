class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ls = []
        for i in range(len(position)):
            ls.append([position[i], speed[i]])
        ls.sort(reverse=True)
        print(ls)
        count = []
        for i in ls:
            count.append((target - i[0]) / i[1])
        l = 0
        r = 1
        print(count)
        # [5, 3, 4, 12]
        while r < len(count):
            if count[r] <= count[l]:
                del count[r]
            else:
                l += 1
                r += 1
        print(count)
        return len(count)
