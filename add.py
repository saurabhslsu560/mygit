class Test:
    def __init__(self,a,b):
        print('constructor level')
        self.x=a
        self.y=b
        return
    def fun1():
        print('class level')
        print(a.x)
        return
    def fun2(self):
        print('object level 1')
        print(self.x)
        return
    def fun3(self):
        print('object level 2')
        self.fun2()
        print(self.y)
        return
a=Test(10,20)
a.fun2()
a.fun3()
Test.fun1()
print(a.x)

