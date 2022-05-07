class Xrange():
    def __init__(self,max_num):
        self.max_num = max_num
    def __iter__(self):
        counter = 0
        while counter <=self.max_num:
            yield counter
            counter +=1

obj = Xrange(100)
for item in obj:
    print(item)