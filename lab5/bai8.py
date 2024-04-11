chuoi = input("Nhập chuỗi (độ dài hơn 10 ký tự): ")

if len(chuoi) <= 10:
    print("Chuỗi phải có độ dài hơn 10 ký tự.")
else:
    # a) Trích ra chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8.
    chuoi_con_a = chuoi[1:8]
    print("a) Chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8:", chuoi_con_a)

    # b) Trích ra chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5.
    chuoi_con_b = chuoi[4:9]
    print("b) Chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5:", chuoi_con_b)

    # c) Trích ra chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự.
    chuoi_con_c = chuoi[-3:]
    print("c) Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", chuoi_con_c)

    # d) Chuyển đổi các ký tự trong chuỗi thành chữ thường.
    chuoi_thuong = chuoi.lower()
    print("d) Chuỗi sau khi chuyển đổi thành chữ thường:", chuoi_thuong)

    # e) Chuyển đổi các ký tự trong chuỗi thành chữ hoa.
    chuoi_hoa = chuoi.upper()
    print("e) Chuỗi sau khi chuyển đổi thành chữ hoa:", chuoi_hoa)

    # f) Đảo ngược chuỗi ký tự vừa nhập.
    chuoi_dao_nguoc = chuoi[::-1]
    print("f) Chuỗi sau khi đảo ngược:", chuoi_dao_nguoc)
