class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        left = 0
        result = 0
        maxFreq = 0

        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1

            maxFreq = max(maxFreq, frequency[s[right]])

            while (right - left + 1) - maxFreq > k:
                frequency[s[left]] -= 1
                left += 1
        
        
            result = max(result, right - left + 1)
        
        return result