so_nguyen = []
tong = 0

while tong <= 1000:
    so = int(input("Nhập một số nguyên dương: "))
    so_nguyen.append(so)
    tong += so

so_le = [so for so in so_nguyen if so % 2 != 0]
so_chan = [so for so in so_nguyen if so % 2 == 0]

print("Các số lẻ đã nhập là:", " ".join(map(str, so_le)))
print("Các số chẵn đã nhập là:", " ".join(map(str, so_chan)))
print("Số lượng các số nguyên đã nhập:", len(so_nguyen))
