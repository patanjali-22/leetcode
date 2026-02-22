#
# Problem: 868. Binary Gap
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-gap/description/?envType=daily-question&envId=2026-02-22
# Language: python3
# Date: 2026-02-22


class Solution(object):
    def binaryGap(self, N):
        last = None
        ans = 0
        for i in range(32):
            if (N >> i) & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i
        return ans
