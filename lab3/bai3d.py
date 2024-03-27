print("Các số hoàn hảo bé hơn 500 là:")
for num in range(1, 500):
    tong_uoc = 0
    for i in range(1, num):
        if num % i == 0:
            tong_uoc += i
    if tong_uoc == num:
        print(num, end=" ")
