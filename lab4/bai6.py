so_chu = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}

number = input("Nhập một số: ")

ket_qua = ""
i = 0
while i < len(number):
    ket_qua += so_chu[number[i]] + " "
    i += 1

print("Số bạn vừa nhập bằng chữ tiếng Việt là:", ket_qua)
