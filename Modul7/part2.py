class A():
    test1 = 1
    def test_n1(self):
        print("In A")

    def fail(self):
        print('Fail')

class D(A):
    def test_n2(self):
        print('In D')

class B(A):
    test2 = 2

    def test_n1(self):
        print('In B')


class C(A, B, D):
    test3 = 3

    def test_n1(self):
        super().test_n1()
        # super(B,self).test_n1()

    def test_n2(self):
        super().test_n2()

    def fail(self):
        super().fail()



c = C()
print(c.test1, c.test2, c.test3)
c.test_n1()
c.test_n2()
