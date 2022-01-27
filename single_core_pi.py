from decimal import Decimal, getcontext
getcontext().prec = 100010

def pi(num):
    n = Decimal(0)
    l = Decimal(13591409)
    x = 1
    m = Decimal(1)
    k = Decimal(-6)
    almostpi = Decimal(0)
    while n < num:
        almostpi += m * l / x
        n += Decimal(1)
        k += Decimal(12)
        l += Decimal(545140134)
        x *= -262537412640768000
        m *= (k ** Decimal(3) - Decimal(16) * k) / (n ** Decimal(3))
        print(n)
    epic = Decimal(426880) * (Decimal(10005) ** Decimal(0.5)) / almostpi
    return epic


print(pi(100000))
input("Finally stopped lmao")