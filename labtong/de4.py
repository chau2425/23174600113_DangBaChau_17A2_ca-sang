import random
import csv

# Kết quả có thể có và xác suất của chúng
xac_suat_ket_qua = {
    "Bang": 0.2,  # Xác suất bắn trúng là 20%
    "Click": 0.8  # Xác suất không bắn trúng là 80%
}

# Set lưu trữ các kết quả có thể có
cac_ket_qua_co_the = set(xac_suat_ket_qua.keys())

# List để lưu trữ kết quả của mỗi lần lắc súng
ket_qua = []

# Hàm để lắc súng
def lac_sung():
    so_ngau_nhien = random.random()  # Số ngẫu nhiên giữa 0 và 1
    xac_suat_tich_luy = 0.0
    for ket_qua, xac_suat in xac_suat_ket_qua.items():
        xac_suat_tich_luy += xac_suat
        if so_ngau_nhien <= xac_suat_tich_luy:
            return ket_qua

# Hàm để tính xác suất xuất hiện của mỗi kết quả
def tinh_xac_suat(ket_qua):
    tong_so_lan_lac = len(ket_qua)
    dem_xac_suat = {kq: 0 for kq in cac_ket_qua_co_the}
    for kq in ket_qua:
        dem_xac_suat[kq] += 1
    
    xac_suat_thuc_te = {kq: dem / tong_so_lan_lac for kq, dem in dem_xac_suat.items()}
    return xac_suat_thuc_te

# Lưu trữ kết quả vào file CSV
def luu_ket_qua_csv(ten_file, ket_qua):
    with open(ten_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Lan Lac", "Ket Qua"])
        for i, kq in enumerate(ket_qua):
            writer.writerow([i + 1, kq])

# Cho phép người chơi lắc súng nhiều lần (tối đa 5 lần)
so_lan_choi = 5

for lan in range(so_lan_choi):
    print(f"Lần lắc súng thứ {lan + 1}:")
    so_lan_lac = 100  # Lắc 100 lần cho mỗi lần chơi
    ket_qua_lan_choi = []

    for _ in range(so_lan_lac):
        ket_qua_lan_choi.append(lac_sung())

    # Lưu kết quả của lần chơi vào danh sách kết quả tổng
    ket_qua.extend(ket_qua_lan_choi)

    # Tính xác suất xuất hiện của mỗi kết quả
    xac_suat_tinh_toan = tinh_xac_suat(ket_qua_lan_choi)

    # In kết quả của lần chơi này
    print(f"Kết quả của mỗi lần lắc súng trong lần chơi thứ {lan + 1}: {ket_qua_lan_choi}")
    print(f"Xác suất xuất hiện của mỗi kết quả trong lần chơi thứ {lan + 1}: {xac_suat_tinh_toan}")
    print()

# Tính toán và hiển thị tổng số kết quả của từng loại kết quả sau 500 lần lắc
dem_ket_qua_tong = {kq: ket_qua.count(kq) for kq in cac_ket_qua_co_the}
print("Tổng số kết quả của từng loại kết quả sau 500 lần lắc:")
print(dem_ket_qua_tong)

# Tính toán và hiển thị xác suất xuất hiện của từng loại kết quả
xac_suat_tong = tinh_xac_suat(ket_qua)
print("Xác suất xuất hiện của từng loại kết quả sau 500 lần lắc:")
print(xac_suat_tong)

# Lưu kết quả vào file CSV
ten_file_csv = "ket_qua_lac_sung.csv"
luu_ket_qua_csv(ten_file_csv, ket_qua)
print(f"Kết quả đã được lưu vào file '{ten_file_csv}'.")
