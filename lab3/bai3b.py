print("Các số chính phương từ 1 đến 1000 là:")
for num in range(1, 1001):
    can_bac_hai = num ** 0.5
    if can_bac_hai == int(can_bac_hai):
        print(num, end=" ")
