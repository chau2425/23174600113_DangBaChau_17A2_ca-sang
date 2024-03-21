def doc_so_nguyen(so):
    don_vi = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    hang_chuc = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    don_vi_special = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    hang_tram = so // 100
    hang_chuc_con_lai = so % 100

    if hang_tram != 0:
        print(don_vi[hang_tram], "hundred", end=" ")

    if hang_chuc_con_lai == 0:
        print("")

    elif hang_chuc_con_lai < 10:
        print(don_vi[hang_chuc_con_lai])

    elif hang_chuc_con_lai < 20:
        print(don_vi_special[hang_chuc_con_lai - 10])

    else:
        hang_chuc_value = hang_chuc[hang_chuc_con_lai // 10]
        don_vi_value = don_vi[hang_chuc_con_lai % 10]
        print(hang_chuc_value, don_vi_value)

so_nguyen = int(input("Nhập một số nguyên có ba chữ số: "))
print("Cách đọc tiếng Anh của số bạn vừa nhập là:")
doc_so_nguyen(so_nguyen)
