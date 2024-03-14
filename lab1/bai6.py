import math

def cong_hai_vector(a, b):
    return [a[i] + b[i] for i in range(len(a))]

def tru_hai_vector(a, b):
    return [a[i] - b[i] for i in range(len(a))]

def do_dai_vector(vector):
    return math.sqrt(sum([x**2 for x in vector]))

def cosin_goc(a, b):
    tich_vo_huong = sum([a[i] * b[i] for i in range(len(a))])
    do_dai_a = do_dai_vector(a)
    do_dai_b = do_dai_vector(b)
    if do_dai_a == 0 or do_dai_b == 0:
        return "Không xác định"
    else:
        return round(tich_vo_huong / (do_dai_a * do_dai_b), 2)

def nhap_vector():
    x = float(input("Nhập tọa độ x: "))
    y = float(input("Nhập tọa độ y: "))
    z = float(input("Nhập tọa độ z: "))
    return [x, y, z]

def main():
    print("Nhập tọa độ của vector a:")
    a = nhap_vector()
    print("Nhập tọa độ của vector b:")
    b = nhap_vector()

    tong_vector = cong_hai_vector(a, b)
    hieu_vector = tru_hai_vector(a, b)
    do_dai_a = do_dai_vector(a)
    do_dai_b = do_dai_vector(b)
    cosin = cosin_goc(a, b)

    print("\n1. Tổng vector a + b:", tong_vector)
    print("   Hiệu vector a - b:", hieu_vector)
    print("\n2. Độ dài của vector a:", round(do_dai_a, 2))
    print("   Độ dài của vector b:", round(do_dai_b, 2))
    print("\n3. Cosin góc giữa hai vector a và b:", cosin)

if __name__ == "__main__":
    main()