class A:### travels left to up then right
    def whom(self):
        print("im in A")
class B(A):
    def whom(self):
        print("im in B")
class C(A):
    def whom(self):
        print("im in C")
class D(B,C):
    pass


class A(object):## travels left to right then up
    def whom(self):
        print("im in A")
class B(A):
    def whom(self):
        print("im in B")
class C(A):
    def whom(self):
        print("im in C")
class D(B,C):
    pass
d1=D()
d1.whom()
