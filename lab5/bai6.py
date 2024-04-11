chuoi = input("Nhập chuỗi: ")
ky_tu_dac_biet = {}
tong_so_ky_tu = len(chuoi)

for ky_tu in chuoi:
    if not ky_tu.isalnum():  # Kiểm tra xem ký tự có phải là ký tự đặc biệt không
        if ky_tu in ky_tu_dac_biet:
            ky_tu_dac_biet[ky_tu] += 1
        else:
            ky_tu_dac_biet[ky_tu] = 1

print("\nKý tự đặc biệt và số lần xuất hiện:")
for ky_tu, dem in ky_tu_dac_biet.items():
    print(f"'{ky_tu}': {dem}")

print("\nTỷ lệ phần trăm của mỗi ký tự đặc biệt trong chuỗi:")
for ky_tu, dem in ky_tu_dac_biet.items():
    ty_le = (dem / tong_so_ky_tu) * 100
    print(f"'{ky_tu}': {ty_le:.2f}%")
