import time

class Foo(object):
    def  __new__(cls, *args, **kwargs):
        # print("__new__ is called: ", cls) #1

        instance = super().__new__(cls)
        # print('instance: ', instance)

        # instance.bar = 10
        return instance

    def __init__(self):
        # print("__init__ is called self: ", self) #2
        # print("self.bar: ", self.bar) #2
        pass

s = Foo()
print(s) #3


# 클래스 변수, 객체 변수
class ClassVar():
    foo = 'foo'

# 인스턴스, 객체 x, 클래스 o
print('ClassVar.foo: ', ClassVar.foo)

ClassVar.foo = 'foo2'
print('ClassVar.foo: ', ClassVar.foo)

cv = ClassVar()
print('cv.foo: ', cv.foo)

print(f'ClassVar.foo: {id(ClassVar.foo)}, cv.foo: {id(cv.foo)}')


# 클래스 메서드

class ClassMethod():

    count = 100
    _protectVar = 'protect'

    @classmethod
    def print_count(cls):
        print('print_count: count', cls.count)
        print('print_count _protectVar: ', cls._protectVar)

ClassMethod.print_count()


class Singleton(object):
    def __new__(cls, *args, **kwargs):

        if hasattr(cls, "_instance"):
            return cls._instance

        # 클래스, 인스턴스(사례), 객체(오브젝트)

        # obj = JconClass()

        # cls (클래스 설계)를 토대로 인스턴스 생성
        cls._instance = super().__new__(cls)

        return cls._instance

        pass

    def __init__(self):
        pass

    def __init__(self):
        self.figures = []
        
    def figure(self):
        fig = time.time()
        self.figures.append(fig)

        return fig

    # def getFigures(self):
    #     return self.figures


s1 = Singleton()
s2 = Singleton()

print('s1: ', s1)
print('s2: ', s2)

s1Figure = s1.figure()
s2Figure = s2.figure()

print('s1 figures: ', s1.getFigures())
print('s2 figures: ', s2.getFigures())