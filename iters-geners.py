class NumberIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            result = self.start
            self.start += 1
            return result
        else:
            raise StopIteration


nums = NumberIterator(1, 2)
for i in nums:
    print (i)

def num_gen(start, end):
    while start < end:
        yield start
        start += 1
a = num_gen(1, 2)
for i in a:
    print(i)


class TextIter:
    def __init__(self, text):
        self.text = text
        self.i = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.text):
            result = self.text[self.i]
            self.i += 1
            return result
        else:
            raise StopIteration


w = TextIter('a')
for i in w:
    print (i)

def num_gen(end):
    for i in range (1, end+1):
        yield pow(i, 2)

a = num_gen(5)
for i in a:
    print(i)

