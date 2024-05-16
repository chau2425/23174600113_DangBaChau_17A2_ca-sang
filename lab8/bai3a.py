def cubesum(n):
    str_n = str(n)
    tong = 0
    for chu_so in str_n:
        chu_so_nguyen = int(chu_so)
        lap_phuong = chu_so_nguyen ** 3
        tong += lap_phuong
    return tong

# Test hàm với ví dụ
n = 123
print(f"Tổng của các lập phương của các chữ số của {n} là: {cubesum(n)}")
