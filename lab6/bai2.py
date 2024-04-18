# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

# Khởi tạo mảng rỗng
mang_so = []

# Nhập giá trị cho từng phần tử
for i in range(n):
  so = int(input(f"Nhập phần tử thứ {i + 1}: "))
  mang_so.append(so)

# Tìm số nguyên tố
so_nguyen_to = []
for so in mang_so:
  if so <= 1:
    continue
  elif so <= 3:
    so_nguyen_to.append(so)
    continue
  elif so % 2 == 0 or so % 3 == 0:
    continue
  i = 5
  while i * i <= so:
    if so % i == 0 or so % (i + 2) == 0:
      break
    i += 6
  else:
    so_nguyen_to.append(so)

# In ra màn hình các số nguyên tố
if so_nguyen_to:
  print("Các số nguyên tố trong mảng:", so_nguyen_to)
else:
  print("Không tìm thấy số nguyên tố nào trong mảng.")

# Tìm số hoàn hảo
so_hoan_hao = []
for so in mang_so:
  if so <= 1:
    continue
  tong_uoc_so = 0
  for i in range(1, so):
    if so % i == 0:
      tong_uoc_so += i
  if tong_uoc_so == so:
    so_hoan_hao.append(so)

# In ra màn hình các số hoàn hảo
if so_hoan_hao:
  print("Các số hoàn hảo trong mảng:", so_hoan_hao)
else:
  print("Không tìm thấy số hoàn hảo nào trong mảng.")
