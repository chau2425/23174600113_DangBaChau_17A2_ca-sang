is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

input_string = input("Nhập chuỗi ký tự: ")
number_string = ''.join(char for char in input_string if char.isdigit())
if number_string:
    number = int(number_string)
    if is_prime(number):
        print(f"{number} là số nguyên tố.")
    else:
        print(f"{number} không phải là số nguyên tố.")
else:
    print("Không có số nào trong chuỗi bạn nhập.")
