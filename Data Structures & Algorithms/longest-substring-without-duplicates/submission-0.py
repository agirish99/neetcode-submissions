class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        largest_window = 0
        seen = set()
        
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])

                current_window = right - left + 1
                largest_window = max(current_window, largest_window)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
                
        return largest_window

            
                