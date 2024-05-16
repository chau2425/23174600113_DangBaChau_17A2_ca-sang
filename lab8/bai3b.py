def cubesum(n):
    str_n = str(n)
    tong = 0
    for chu_so in str_n:
        chu_so_nguyen = int(chu_so)
        lap_phuong = chu_so_nguyen ** 3
        tong += lap_phuong
    return tong

def isArmstrong(n):
    return n == cubesum(n)

def PrintArmstrong():
    for i in range(1000):
        if isArmstrong(i):
            print(i)

# Test các hàm
print("Các số Armstrong từ 0 đến 999 là:")
PrintArmstrong()
