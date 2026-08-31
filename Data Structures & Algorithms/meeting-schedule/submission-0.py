"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda intervals: intervals.start)
        print('length:',len(intervals))

        for i in range(1, len(intervals)):  #Start from second meeting
            previous = intervals[i-1]
            current = intervals[i]

            if previous.end > current.start:
                return False

            print('current:', current.start, current.end)
            print('previous:',previous.start, previous.end)

        return True

        
