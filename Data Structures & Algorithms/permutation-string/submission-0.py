class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequencyS1 = {}
        left = 0 
        window = {} #Frequency within the window

        for char in s1:
            frequencyS1[char] = frequencyS1.get(char, 0) + 1

        for right in range(len(s2)):
            char = s2[right]
            window[char] = window.get(char, 0) + 1

            if (right - left + 1) > len(s1):
                left_char = s2[left]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

                left += 1

            if window == frequencyS1:
                return True

        return False
        