class A:
    pass

class B:
    pass

class C(A, B):
    pass
# --------------------------------------------------------------------------------------------------------------------------
class Fly:
    def fly(self):
        print("I can fly")

class Swim:
    def swim(self):
        print("I can swim")

class Duck(Fly, Swim):
    pass

d = Duck()
d.fly()
d.swim()
# --------------------------------------------------------------------------------------------------------------------------
class A:
    def hello(self):
        print("A")

class B:
    def hello(self):
        print("B")

class C(A, B):
    pass

C().hello()
# --------------------------------------------------------------------------------------------------------------------------
