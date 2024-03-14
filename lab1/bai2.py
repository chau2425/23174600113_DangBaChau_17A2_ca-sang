def main():
    # Nhập thông tin sách từ người dùng
    so_luong_sach = input("Nhập số lượng sách (ngày sinh của sinh viên): ")
    ma_sach = input("Nhập mã sách (mã sinh viên): ")
    ten_sach = input("Nhập tên sách (tùy chọn): ")
    tac_gia = input("Nhập tác giả (tác giả theo sách đã chọn): ")
    nam_xuat_ban = input("Nhập năm xuất bản (năm xuất bản theo sách đã chọn): ")

    # In ra thông tin sách
    print(f"Thư viện ĐHKTKTCN có {so_luong_sach} sách {ten_sach} với mã số {ma_sach}.")
    print(f"Cuốn sách của tác giả {tac_gia} được xuất bản vào năm {nam_xuat_ban}.")

if __name__ == "__main__":
    main()