# Khởi tạo hai số Fibonacci đầu tiên
a, b = 0, 1

print("Các số Fibonacci nhỏ hơn 1000 là:")
while a < 1000:
    print(a, end=" ")
    a, b = b, a + b
