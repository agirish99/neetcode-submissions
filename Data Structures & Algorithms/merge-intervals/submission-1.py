class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda intervals: intervals[0])
        merged = [intervals[0]] #hyrdate with first interval as this will always exist
        print(merged)
        for i in range(1, len(intervals)):
            previous = merged[-1]
            current = intervals[i]

            if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])
            else:
                merged.append(current)

        return merged
        