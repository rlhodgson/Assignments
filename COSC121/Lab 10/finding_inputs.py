class Thing:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        return "{}, {}".format(self.a, self.b)

    def mangle(self):
        temp = self.a
        self.a = self.b + self.a + self.a + self.b
        self.b = temp + self.b + self.b + temp
        
def gaga(obj):
    obj.mangle()
    print(obj)
    
class Another:
    def __init__(self, x):
        self.a = x
        self.count = 0

    def __str__(self):
        return "{}, {}".format(len(self.a), sum(self.a))

    def twiddle(self):
        self.count += 1
        self.a.append(self.count)
        
def sigh(x):
    x.twiddle()
    x.twiddle()
    x.twiddle()
    print(x)
    
num = Another([194, 300, 500])
sigh(num)
