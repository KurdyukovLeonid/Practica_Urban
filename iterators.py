class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        if self.i < self.end:
            self.i += 2
            return self.i
        raise StopIteration

result = EvenNumbers(10, 25)
for i in result:
    print(i)
