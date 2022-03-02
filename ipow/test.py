def test_ipow_returns_not_implemented(self):
    class A:
        def __ipow__(self, other):
            return NotImplemented

    class B(A):
        def __rpow__(self, other):
            return 1

    class C(A):
        def __pow__(self, other):
            return 2
    a = A()
    b = B()
    c = C()

    a **= b
    print(a == 1)

    c **= b
    print(c == 2)


def test_no_ipow(self):
    class B:
        def __rpow__(self, other):
            return 1

    a = object()
    b = B()
    a **= b
    print(a == 1)



def main():
    test_no_ipow(1)
    test_ipow_returns_not_implemented(1)


if __name__ == '__main__':
    main()