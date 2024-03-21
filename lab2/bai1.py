def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -b / a
        print("Nghiệm của phương trình là:", x)

# Nhập các hệ số từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

# Gọi hàm để giải phương trình và biện luận
print("Phương trình bạn đã nhập là:", a, "x +", b, "= 0")
giai_phuong_trinh_bac_nhat(a, b)