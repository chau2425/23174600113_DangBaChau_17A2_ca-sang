def sumPdivisors(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

# Test hàm với ví dụ
n = 36
print(f"Tổng của các ước số chính của {n} là: {sumPdivisors(n)}")
