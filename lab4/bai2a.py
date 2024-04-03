so_nguyen = 2
print("Các số nguyên tố nhỏ hơn 100 là:")
while so_nguyen < 100:
    la_so_nguyen_to = True
    if so_nguyen <= 1:
        la_so_nguyen_to = False
    else:
        uoc_so = 2
        while uoc_so * uoc_so <= so_nguyen:
            if so_nguyen % uoc_so == 0:
                la_so_nguyen_to = False
                break
            uoc_so += 1
    if la_so_nguyen_to:
        print(so_nguyen, end=" ")
    so_nguyen += 1
