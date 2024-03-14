import math

def main():
    # Nhập chiều dài cạnh đáy và chiều cao từ người dùng
    canh_day = float(input("Nhập độ dài cạnh đáy của hình chóp đều: "))
    chieu_cao = float(input("Nhập chiều cao của hình chóp đều: "))

    # Tính toán diện tích xung quanh
    dien_tich_xung_quanh = 4 * canh_day * chieu_cao

    # Tính toán diện tích toàn phần
    dien_tich_toan_phan = dien_tich_xung_quanh + (0.5 * math.sqrt(3) * canh_day ** 2)

    # Tính toán thể tích
    the_tich = (1 / 3) * math.sqrt(3) * canh_day ** 2 * chieu_cao

    # In kết quả
    print("Diện tích xung quanh của hình chóp đều là:", round(dien_tich_xung_quanh, 2))
    print("Diện tích toàn phần của hình chóp đều là:", round(dien_tich_toan_phan, 2))
    print("Thể tích của hình chóp đều là:", round(the_tich, 2))

if __name__ == "__main__":
    main()