string1 = input("Nhập chuỗi ký tự thứ nhất: ")
string2 = input("Nhập chuỗi ký tự thứ hai: ")

merged_string = ''
length1 = len(string1)
length2 = len(string2)
max_length = max(length1, length2)

for i in range(max_length):
    if i < length1:
        merged_string += string1[i]
    if i < length2:
        merged_string += string2[i]
    if i < max_length - 1:  # không thêm dấu gạch nối sau khi đã kết thúc chuỗi
        merged_string += '-'

print("Chuỗi kết quả sau khi trộn hai chuỗi là:", merged_string)
