so_thap_phan = int(input("Nhập số thập phân: "))
so_nhi_phan = ""

while so_thap_phan > 0:
  so_du = so_thap_phan % 2
  so_thap_phan //= 2
  so_nhi_phan = str(so_du) + so_nhi_phan

print(f"Số nhị phân của {so_thap_phan} là: {so_nhi_phan}")
