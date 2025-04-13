# 示範模除與餘數的關係
# 裝飾器@在python的使用方法

from time import perf_counter  # 改用更精準的 perf_counter


def time_counting_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = func(*args, **kwargs)
        t2 = perf_counter()
        print(f"{t2}-{t1} = {t2 - t1:.6f} seconds")  # 顯示到小數點後 6 位
        return result
    return wrapper


@time_counting_decorator
def mod_calculate():

    x = int(-1)
    for a in range(0, n*5+1):
        if a % n == 0:
            x += 1
        print(f"{a:3} % {n}  mod:{a%n:>3}     {a:3} = {x} * {n} + {a%n:3}       {a:3} ÷ {n:>3} :  diviser: {x}   remainder:{a%n:>3}")


while True:
    try:
        n = int(input("輸入用於取模的數: "))
        if n > 0:
            break  # 是正整數，跳出迴圈
        else:
            print("請輸入正整數！")
    except ValueError:
        print("請輸入有效的整數！")

print(mod_calculate())
