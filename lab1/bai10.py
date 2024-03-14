from math import comb

def xac_suất_tất_cả_là_bi_đỏ(tổng_số_bi, số_bi_đỏ, số_bi_rút):
    return comb(số_bi_đỏ, số_bi_rút) / comb(tổng_số_bi, số_bi_rút)

def xac_suất_ít_nhất_một_bi_xanh(tổng_số_bi, số_bi_xanh, số_bi_khác, số_bi_rút):
    return 1 - comb(số_bi_khác, số_bi_rút) / comb(tổng_số_bi, số_bi_rút)

def xac_suất_chính_xác_hai_bi_vàng(tổng_số_bi, số_bi_vàng, số_bi_rút):
    return (comb(số_bi_vàng, 2) * comb(tổng_số_bi - số_bi_vàng, số_bi_rút - 2)) / comb(tổng_số_bi, số_bi_rút)

def main():
    tổng_số_bi = 50
    số_bi_đỏ = 20
    số_bi_xanh = 15
    số_bi_vàng = 15

    số_bi_rút = int(input("Nhập số lượng bi bạn muốn rút ra từ hộp: "))

    xác_suất_1 = xac_suất_tất_cả_là_bi_đỏ(tổng_số_bi, số_bi_đỏ, số_bi_rút)
    xác_suất_2 = xac_suất_ít_nhất_một_bi_xanh(tổng_số_bi, số_bi_xanh, số_bi_đỏ + số_bi_vàng, số_bi_rút)
    xác_suất_3 = xac_suất_chính_xác_hai_bi_vàng(tổng_số_bi, số_bi_vàng, số_bi_rút)

    print("Xác suất để:")
    print("1. Tất cả là bi đỏ: {:.4f}".format(xác_suất_1))
    print("2. Ít nhất một viên là bi xanh: {:.4f}".format(xác_suất_2))
    print("3. Đúng hai viên là bi vàng: {:.4f}".format(xác_suất_3))

if __name__ == "__main__":
    main()