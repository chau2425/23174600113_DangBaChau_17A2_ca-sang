n = int(input("Nhập vào số nguyên n (n > 10): "))

while n <= 10:
    n = int(input("Nhập lại số nguyên n (n > 10): "))

a = 6
tong = 0
i = 1

while a <= n:
    tong += a
    a *= 6
    i += 1

print("Tổng S1 =", tong)
