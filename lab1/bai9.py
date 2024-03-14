def tinh_trung_diem(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

def nhap_toa_do_dinh():
    dinh = []
    for i in range(4):
        x = float(input(f"Nhập tọa độ x của điểm {chr(65 + i)}: "))
        y = float(input(f"Nhập tọa độ y của điểm {chr(65 + i)}: "))
        dinh.append((x, y))
    return dinh

def main():
    dinh = nhap_toa_do_dinh()

    print("\nTọa độ trung điểm của mỗi cạnh của tứ giác:")
    for i in range(4):
        j = (i + 1) % 4  # Đỉnh tiếp theo
        trung_diem = tinh_trung_diem(dinh[i], dinh[j])
        print(f"Trung điểm của cạnh {chr(65 + i)}{chr(65 + j)} là: {trung_diem}")

if __name__ == "__main__":
    main()

