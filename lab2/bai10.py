def chon_suatchieu(theloai, thoigian):
    if theloai == "Hành động" or theloai == "Hài hước":
        if thoigian == "sáng" or thoigian == "trưa" or thoigian == "chiều" or thoigian == "tối":
            return "Phim " + theloai + " được chiếu vào thời gian " + thoigian
        else:
            return "Không có suất chiếu"
    elif theloai == "Kinh dị":
        if thoigian == "tối":
            return "Phim " + theloai + " được chiếu vào thời gian " + thoigian
        else:
            return "Không có suất chiếu"
    elif theloai == "Tình cảm":
        if thoigian == "tối":
            return "Phim " + theloai + " được chiếu vào thời gian " + thoigian
        else:
            return "Không có suất chiếu"
    elif theloai == "Hoạt hình":
        if thoigian == "sáng" or thoigian == "trưa":
            return "Phim " + theloai + " được chiếu vào thời gian " + thoigian
        else:
            return "Không có suất chiếu"
    else:
        return "Thể loại không hợp lệ"

def main():
    print("Chào mừng bạn đến với hệ thống đặt vé xem phim!")
    print("Danh sách thể loại phim: Hành động, Kinh dị, Tình cảm, Hài hước, Hoạt hình")
    theloai = input("Nhập thể loại phim bạn muốn xem: ")
    thoigian = input("Nhập thời gian bạn muốn xem phim (sáng, trưa, chiều, tối): ")

    ketqua = chon_suatchieu(theloai, thoigian)
    print(ketqua)

if __name__ == "__main__":
    main()
