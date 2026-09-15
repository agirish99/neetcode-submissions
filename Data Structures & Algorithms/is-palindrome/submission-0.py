class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char.lower() for char in s if char.isalnum())
        print(cleaned_text)

        left = 0
        right = len(cleaned_text) - 1

        while left < right:
            if cleaned_text[left] != cleaned_text[right]:
                return False
            left += 1
            right -=1

        return True