n = int(input("Nhập vào số nguyên n (n > 0): "))

while n <= 0:
    n = int(input("Nhập lại số nguyên n (n > 0): "))

tong = 0
i = 1

while i <= n:
    tong += ((-1)**i) * (i**2)
    i += 1

print("Tổng S =", tong)
