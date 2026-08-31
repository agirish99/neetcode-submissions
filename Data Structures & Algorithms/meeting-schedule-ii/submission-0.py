"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval:interval.start)
        rooms = []

        for i in intervals:
            if rooms and i.start >= rooms[0]:
                heapq.heappop(rooms) # removes the earliest room as its available to use
            heapq.heappush(rooms, i.end)

        return len(rooms)