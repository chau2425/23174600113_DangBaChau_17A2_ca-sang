def chuso_hang_nghin(so):
    if so >= 1000:
        chuso = so // 1000
        print("Chữ số hàng nghìn của số", so, "là:", chuso)
    else:
        print("Số không có chữ số hàng nghìn, xuất ra 0.")

so_nguyen = int(input("Nhập một số nguyên: "))
chuso_hang_nghin(so_nguyen)