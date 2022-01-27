from decimal import Decimal, getcontext
from math import comb, sqrt
import multiprocessing
from functools import partial
from timeit import default_timer as timer
def pi(num,q,i):
    almostpi = Decimal(0)
    n = i
    l = Decimal(545140134 * i + 13591409)
    x = (-262537412640768000) ** i
    m = comb(4 * i, i) * comb(5 * i, i) * comb(6 * i, i)
    num1 = Decimal(545140134 * q)
    num2 = (-262537412640768000) ** q
    while n < num:
        almostpi += m * l / x
        n += q
        l += num1
        x *= num2
        m = comb(4 * n, n) * comb(5 * n, n) * comb(6 * n, n)
        print(n)
    return almostpi
def cardano(a1, b1, c1, d1):
    p = (c1-(b1**2)/(3*a1))/a1
    q = (d1 + 2*(b1**3)/(27*(a1**2)) - b1*c1/(3*a1))/a1
    ans1 = (-1*q/2+sqrt((q**3)/4+(p**3)/27))**(1/3) - b1/3
    ans2 = (-1*q/2-sqrt((q**3)/4+(p**3)/27))**(1/3) - b1/3
    ans3 = ans1 + ans2 + b1/3
    return(ans1, ans2, ans3)
if __name__ == "__main__":
    acc = int(input("accuracy: "))
    getcontext().prec = acc + 10
    cores = input("cores to use (leave empty if you want half of them): ")
    i = input("n to start from (only use this if you know what you're doing): ")
    gpu = input("do you want to use the gpu or cpu? (can only work with the package for it installed and a nvidia gpu) 1-cpu, 2-gpu:")
    if gpu == "1":
        if cores == "":
            q = int(multiprocessing.cpu_count() / 2)
        else:
            q = int(cores)
        if i == "":
            i = 0
        else:
            i = int(i)
        pool = multiprocessing.Pool(q)
        corelist = list(range(i,q))
        a = 2E-8
        b = 4E-6
        c = 0.0008
        xMax = acc/10
        sMax = a/3*xMax**3+b/2*xMax**2+c*xMax
        for n in range(1,q):
            answer = cardano(a/3, b/2, c, -1*sMax*n/q)
            print(answer)
    if gpu == "2":
        print("nah fuck you")