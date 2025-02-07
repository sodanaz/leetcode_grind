'''stones = "aAAbbbb"

stones_set = set(stones)
print(stones_set)
print('z'=='Z')''' # some testings here

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        count = 0
        for i in stones:
            if i in jewels_set:
                count += 1
        return count # s pervogo raza poluchilos' ksta ahahahha

