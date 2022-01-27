from decimal import Decimal, getcontext
from matplotlib import pyplot as plt
from timeit import default_timer as timer
import pandas as pd
getcontext().prec = 10010

def pi(num):
    n = Decimal(0)
    l = Decimal(13591409)
    x = 1
    m = Decimal(1)
    k = Decimal(-6)
    almostpi = Decimal(0)
    epiclist = []
    while n < num:
        start = timer()
        almostpi += m * l / x
        n += Decimal(1)
        k += Decimal(12)
        l += Decimal(545140134)
        x *= -262537412640768000
        m *= (k ** Decimal(3) - Decimal(16) * k) / (n ** Decimal(3))
        epiclist.append(timer() - start)
        print(n)
    return epiclist

times = pi(1000)
print(times)
df = pd.DataFrame(times)
df.to_csv("points.csv")
plt.plot(list(range(len(times))),times)
plt.legend()
plt.show()
input("Finally stopped lmao")