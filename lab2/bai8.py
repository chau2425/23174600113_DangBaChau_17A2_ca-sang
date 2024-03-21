def xac_dinh_vi_tri_duong_thang(m1, b1, m2, b2):
    if m1 == m2:
        return "Hai đường thẳng là đường thẳng song song."
    
    if m1 == -m2:
        return "Hai đường thẳng là đường thẳng vuông góc."
    
    return "Hai đường thẳng cắt nhau."

def main():
    try:
        m1 = float(input("Nhập hệ số góc của đường thẳng thứ nhất: "))
        b1 = float(input("Nhập hệ số tự do của đường thẳng thứ nhất: "))
        m2 = float(input("Nhập hệ số góc của đường thẳng thứ hai: "))
        b2 = float(input("Nhập hệ số tự do của đường thẳng thứ hai: "))
        
        vi_tri = xac_dinh_vi_tri_duong_thang(m1, b1, m2, b2)
        print("Vị trí tương đối của hai đường thẳng là:", vi_tri)
    except ValueError:
        print("Vui lòng nhập các số thực.")

if __name__ == "__main__":
    main()
