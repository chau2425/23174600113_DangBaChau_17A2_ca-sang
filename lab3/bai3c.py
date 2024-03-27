a, b = 0, 1
print("Chuỗi Fibonacci sao cho số cuối cùng nhỏ hơn 100 là:")
print(a, end=" ")
while b < 100:
    print(b, end=" ")
    a, b = b, a + b
