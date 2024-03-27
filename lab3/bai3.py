print("Các số nguyên tố từ 100 đến 1000 là:")
for num in range(100, 1001):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
