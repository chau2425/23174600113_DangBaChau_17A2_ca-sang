# Nhập dãy số
while True:
    try:
        dãy_so = [int(x) for x in input("Nhập dãy số nguyên, ngăn cách nhau bởi dấu phẩy: ").split(",")]
        if len(dãy_so) < 2:
            raise ValueError("Cần nhập ít nhất 2 số!")
        break
    except ValueError:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập dãy số nguyên, ngăn cách nhau bởi dấu phẩy.")

# Khởi tạo biến kiểm tra cấp số cộng
is_arithmetic_progression = True

# Khởi tạo biến lưu trữ công sai (nếu có)
common_difference = None

# Duyệt qua dãy số từ phần tử thứ hai
for i in range(1, len(dãy_so)):
    # Tính toán công sai nếu chưa có
    if common_difference is None:
        common_difference = dãy_so[i] - dãy_so[i - 1]

    # Kiểm tra công sai giữa các phần tử liền kề
    else:
        if dãy_so[i] - dãy_so[i - 1] != common_difference:
            is_arithmetic_progression = False
            break

# Xuất kết quả
if is_arithmetic_progression:
    print(f"Dãy số {dãy_so} là cấp số cộng với công sai {common_difference}.")
else:
    print(f"Dãy số {dãy_so} không phải là cấp số cộng.")
