# Khai báo từ điển kho
kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

# Khai báo từ điển giá tiền
gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Khởi tạo hóa đơn
hoa_don = {}

# Tính hóa đơn khi mua hàng
for item in kho:
    so_luong = kho[item]
    don_gia = gia_tien[item]
    thanh_tien = so_luong * don_gia
    hoa_don[item] = {'so_luong': so_luong, 'don_gia': don_gia, 'thanh_tien': thanh_tien}

# Tính tổng số tiền của hóa đơn
tong_tien = sum(hoa_don[item]['thanh_tien'] for item in hoa_don)

# In hóa đơn
print("Hóa đơn mua hàng:")
for item in hoa_don:
    print(f"Mặt hàng: {item}, Số lượng: {hoa_don[item]['so_luong']}, Đơn giá: {hoa_don[item]['don_gia']}, Thành tiền: {hoa_don[item]['thanh_tien']}")

print(f"Tổng số tiền của hóa đơn: {tong_tien}")

# In lại số lượng của các mặt hàng trong kho sau khi đã mua
print("\nSố lượng của các mặt hàng trong kho sau khi đã mua:")
for item in kho:
    print(f"{item}: {kho[item]}")
