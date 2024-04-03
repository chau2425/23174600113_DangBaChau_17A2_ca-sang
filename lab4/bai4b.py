n = int(input("Nhập vào số nguyên n (n > 0): "))

while n <= 0:
    n = int(input("Nhập lại số nguyên n (n > 0): "))

tong = 0
i = 0

tong += 1

while i < n:
    tong += 1 / (3**(2*i + 1))
    i += 1

print("Tổng S2 =", tong)
