# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

# Khởi tạo mảng rỗng
mang_so = []

# Nhập giá trị cho từng phần tử
for i in range(n):
  so = int(input(f"Nhập phần tử thứ {i + 1}: "))
  mang_so.append(so)

# Khởi tạo biến để lưu trữ tổng số chẵn và lẻ
tong_chan = 0
tong_le = 0

# Duyệt qua từng phần tử trong mảng
for so in mang_so:
  # Kiểm tra số chẵn hay lẻ
  if so % 2 == 0:
    tong_chan += so
  else:
    tong_le += so

# Xuất kết quả
print(f"Tổng các số chẵn: {tong_chan}")
print(f"Tổng các số lẻ: {tong_le}")
