try:
    N = int(input("Nhập số nguyên N: "))
    if N <= 0:
        print("Vui lòng nhập một số nguyên dương.")
    else:
        dictionary = {}
        for i in range(1, N+1):
            dictionary[i] = i ** 3

        print("Từ điển dạng key: value (x: x^3):")
        for key, value in dictionary.items():
            print(f"{key}: {value}")
except ValueError:
    print("Vui lòng chỉ nhập số nguyên")
