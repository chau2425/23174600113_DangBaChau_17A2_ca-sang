def main():
    so_gio_su_dung = float(input("Nhập số giờ sử dụng máy lọc không khí: "))

    cong_suat = 220 * 1.5

    cong_suat_tieu_thu = cong_suat / 1000

    gia_dien = 5000

    tong_tien_dien = cong_suat_tieu_thu * so_gio_su_dung * gia_dien

    print("Tổng số tiền điện phải trả cho việc sử dụng máy lọc không khí là:", round(tong_tien_dien, 2), "đồng")

if __name__ == "__main__":
    main()