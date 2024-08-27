class Iter:
    def __init__(self, num):
        self.count = 0
        self.num = num

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.count += (self.num - (self.num - 1))
        if self.count > self.num:
            raise StopIteration()
        return self.count


itr = Iter(5)
for i in itr:
    print(i)
