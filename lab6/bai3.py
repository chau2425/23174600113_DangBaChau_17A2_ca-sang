# Nhập số lượng phần tử
so_luong_phan_tu = int(input("Nhập số lượng phần tử: "))

# Khởi tạo danh sách rỗng để lưu trữ dãy số
dãy_so = []

# Nhập số lượng phần tử và các phần tử trong dãy số
for i in range(so_luong_phan_tu):
  try:
    so = float(input(f"Nhập phần tử thứ {i + 1}: "))
    dãy_so.append(so)
  except ValueError:
    print("Giá trị nhập vào không hợp lệ. Vui lòng nhập số!")

# Tìm số lớn nhất và nhỏ nhất
so_lon_nhat = dãy_so[0]
so_nho_nhat = dãy_so[0]
for so in dãy_so:
  if so > so_lon_nhat:
    so_lon_nhat = so
  if so < so_nho_nhat:
    so_nho_nhat = so

# In ra màn hình kết quả
print(f"Số lớn nhất trong dãy số là: {so_lon_nhat}")
print(f"Số nhỏ nhất trong dãy số là: {so_nho_nhat}")
