# Scenario: A ticket counter provides ticket numbers one at a time.
class TicketCounter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        ticket = self.current
        self.current += 1
        return f"T-{ticket:03d}"

for ticket in TicketCounter(1, 5):
    print("Issued:", ticket)
