import math

def hoan_vi(n, r):
    if n < r or n < 0 or r < 0:
        return "Giá trị không hợp lệ"
    return math.factorial(n) // math.factorial(n - r)

def to_hop(n, r):
    if n < r or n < 0 or r < 0:
        return "Giá trị không hợp lệ"
    return hoan_vi(n, r) // math.factorial(r)

# Test chương trình với các giá trị cụ thể
n = 5
r = 3

print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần là: p({n}, {r}) = {hoan_vi(n, r)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần là: c({n}, {r}) = {to_hop(n, r)}")
