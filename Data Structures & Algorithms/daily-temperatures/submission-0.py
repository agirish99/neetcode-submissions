class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  #store of temperature index waiting for a warmer day
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = i - previous_index #number of days till warmer day
            stack.append(i)

        return result
        
        