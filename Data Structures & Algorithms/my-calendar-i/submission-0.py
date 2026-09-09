class MyCalendar:
    
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.events:
            if not (startTime >= end or endTime <= start):
                return False

        self.events.append((startTime, endTime))
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)