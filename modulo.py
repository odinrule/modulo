# 示範模除與餘數的關係
# 裝飾器@在python的使用方法

from time import time


def time_counting_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func()
        t2 = time()
        return (f"{t2}-{t1}={(t2-t1)}seconds")
    return wrapper


@time_counting_decorator
def mod_calculate():
    n = int(input("輸入用於取模的數:"))
    n = int(n)  # 取模的數 , 除數

    x = int(-1)
    for a in range(0, n*5+1):
        if a % n == 0:
            x += 1
        print(f"{a:3} % {n}  mod:{a%n:>3}     {a:3} = {x} * {n} + {a%n:3}       {a:3} ÷ {n:>3} :  diviser: {x}   remainder:{a%n:>3}")


print(mod_calculate())
