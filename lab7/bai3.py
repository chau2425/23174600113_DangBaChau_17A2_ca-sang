# Nhập văn bản từ người dùng
text = input("Nhập văn bản: ")

# Chuyển văn bản thành danh sách các từ
words = text.split()

# Khởi tạo từ điển để lưu số lần xuất hiện của mỗi từ
word_count = {}

# Đếm số lần xuất hiện của mỗi từ
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Tìm từ có số lượng nhiều nhất và ít nhất
most_common_word = max(word_count, key=word_count.get)
least_common_word = min(word_count, key=word_count.get)

# In ra từ có số lượng nhiều nhất và ít nhất
print(f"Từ có số lượng nhiều nhất là '{most_common_word}' với {word_count[most_common_word]} lần.")
print(f"Từ có số lượng ít nhất là '{least_common_word}' với {word_count[least_common_word]} lần.")
