class Bar(object):

    def __init__(self):
        self.value = '101'
        print("in init method" + self.value)

    def __get__(self, instance, owner):
        print("returned from descriptor object")
        return self.value

    def __set__(self, instance, value):
        print("set in descriptor object")
        self.value = value


    def __delete__(self, instance):
        print("deleted in descriptor object")
        del self.value

class Foo(object):
    print('in foo class')
    bar = Bar()


f = Foo()
print(f.bar)
f.bar = 10
print('after setting 10')
print(f.bar)
