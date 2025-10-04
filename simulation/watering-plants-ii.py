class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ca, cb = capacityA, capacityB
        a, b = 0, len(plants)-1
        ans = 0
        while a < b:
            # Alice
            if ca >= plants[a]:
                ca -= plants[a]
                a += 1
            else: # ca < plants[a]
                ca = capacityA
                ans += 1
                ca -= plants[a]
                a += 1
            # Bob
            if cb >= plants[b]:
                cb -= plants[b]
                b -= 1
            else:
                cb = capacityB
                ans += 1
                cb -= plants[b]
                b -= 1
        if a == b and max(ca, cb) < plants[a]:
            ans += 1
        
        return ans