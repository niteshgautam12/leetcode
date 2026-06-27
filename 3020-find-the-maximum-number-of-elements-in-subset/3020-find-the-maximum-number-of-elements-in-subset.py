class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        ans = 1
        if 1 in freq:
            if freq[1] % 2 == 0:
                ans = freq[1] - 1
            else:
                ans = freq[1]
        for num in freq:
            if num == 1:
                continue

            curr = num
            length = 0

            while freq[curr] >= 2:
                length += 2
                curr = curr * curr

            if freq[curr] == 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans