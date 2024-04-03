so_nguyen = int(input("Nhập vào một số nguyên: "))
so_chu_so = 0

if so_nguyen == 0:
    so_chu_so = 1
else:
    so_nguyen = abs(so_nguyen)

while so_nguyen > 0:
    so_nguyen //= 10
    so_chu_so += 1

print("Số chữ số của số nguyên là:", so_chu_so)
