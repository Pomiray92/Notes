# f(0) = 1
# f(1) = 1
# f(n) = f(n - 1) + f(n - 2)
def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(6))