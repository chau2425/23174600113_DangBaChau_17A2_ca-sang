# Khởi tạo từ điển để lưu thông tin của sinh viên
student_info = {}

# Nhập thông tin của 10 sinh viên từ bàn phím
for i in range(1, 11):
    name = input(f"Nhập tên của sinh viên thứ {i}: ")
    while True:
        try:
            score = float(input(f"Nhập điểm thi của sinh viên {name}: "))
            if 0.0 <= score <= 10.0:
                student_info[name] = score
                break
            else:
                print("Điểm thi phải nằm trong khoảng từ 0.0 đến 10.0.")
        except ValueError:
            print("Vui lòng nhập điểm thi là một số.")

# Khởi tạo từ điển để lưu số lượng sinh viên theo loại học lực
grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

# Xếp loại học lực của từng sinh viên và thống kê số lượng sinh viên ở mỗi loại học lực
for student, score in student_info.items():
    if score >= 8.5:
        grade_count['A'] += 1
    elif score >= 7.0:
        grade_count['B'] += 1
    elif score >= 5.5:
        grade_count['C'] += 1
    elif score >= 4.0:
        grade_count['D'] += 1
    else:
        grade_count['F'] += 1

# In ra xếp loại học lực của từng sinh viên
print("\nXếp loại học lực của sinh viên:")
for student, score in student_info.items():
    if score >= 8.5:
        print(f"{student}: A")
    elif score >= 7.0:
        print(f"{student}: B")
    elif score >= 5.5:
        print(f"{student}: C")
    elif score >= 4.0:
        print(f"{student}: D")
    else:
        print(f"{student}: F")

# In ra thống kê số lượng sinh viên ở mỗi loại học lực
print("\nThống kê số lượng sinh viên ở mỗi loại học lực:")
for grade, count in grade_count.items():
    print(f"{grade}: {count}")
